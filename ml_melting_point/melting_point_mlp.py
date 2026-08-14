import warnings
warnings.filterwarnings("ignore")

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.inspection import permutation_importance

import numpy as np

from descriptors import calculate_descriptors, FEATURE_NAMES

# Load data from CSV file
data = pd.read_csv('melting_points.csv')  # Replace 'training_data.csv' with your actual file

# Generate molecular descriptors from SMILES strings, dropping any rows that fail to parse
data['Descriptors'] = data['smiles'].apply(calculate_descriptors)
data = data[data['Descriptors'].notna()].reset_index(drop=True)

# Split the data into features and target variable
X = pd.DataFrame(data['Descriptors'].tolist(), columns=FEATURE_NAMES)
y = data['mp']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define hyperparameters grid for GridSearchCV
param_grid = {
    'hidden_layer_sizes': [(50,), (100,), (100, 50), (200, 100)],
    'activation': ['relu', 'tanh'],
    'solver': ['adam', 'sgd'],
    'alpha': [0.0001, 0.001, 0.01]
}

mlp_regressor = MLPRegressor(max_iter=1000, random_state=42)

# Perform GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(mlp_regressor, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=8)
grid_search.fit(X_train_scaled, y_train)

# Get the best model from the grid search
best_mlp_model = grid_search.best_estimator_

# Print the optimal hyperparameters
print("Optimal Hyperparameters:")
print(grid_search.best_params_)

# Predict melting points using the best model
y_pred = best_mlp_model.predict(X_test_scaled)

# Write predicted melting points to a file                                                                                                                   
with open('predicted_melting_points_mlp.csv', 'w') as fhout:
    fhout.write('SMILES' + ',' + 'Target_MP' + ',' + 'Predicted_MP' + '\n')
    for smi, y_true, y_pred_ in zip(data.loc[y_test.index, 'smiles'], y_test, y_pred):
        fhout.write(f"{smi},{y_true},{y_pred_}\n")

fhout.close()

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Coefficient of Determination (R^2): {r2}')

# Perform feature permutation importance (on the scaled features the model was trained on)
perm_importance = permutation_importance(best_mlp_model, X_test_scaled, y_test, n_repeats=10, random_state=42)

# Get feature importances
feature_importances = perm_importance.importances_mean


# Get feature names
feature_names = X.columns
print()
# Sort feature importances
sorted_indices = feature_importances.argsort()[::-1]

# Print top 10 feature importances
print("Top 10 Most Important Features:")
for index in sorted_indices[:10]:
    print(f'{feature_names[index]}: {feature_importances[index]}')

model_path = 'melting_point_mlp_model.joblib'
joblib.dump({
    'model': best_mlp_model,
    'scaler': scaler,
    'feature_names': FEATURE_NAMES,
    'model_name': 'MLP Regressor',
}, model_path)
print(f"\nSaved best model to {model_path}")
