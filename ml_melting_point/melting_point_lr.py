import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

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

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Perform GridSearchCV for hyperparameter tuning
param_grid = {'alpha': [0.1, 1, 10]}
grid_search = GridSearchCV(Ridge(), param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=8)
grid_search.fit(X_train_scaled, y_train)

best_ridge_model = grid_search.best_estimator_

y_pred = best_ridge_model.predict(X_test_scaled)

# Write predicted melting points to a file

with open('predicted_melting_points_lr.csv', 'w') as fhout:
    fhout.write('SMILES' + ',' + 'Target_MP' + ',' + 'Predicted_MP' + '\n')
    for smi, y_true, y_pred_ in zip(data.loc[y_test.index, 'smiles'], y_test, y_pred):
        fhout.write(f"{smi},{y_true},{y_pred_}\n")
    fhout.close()
    
# Calculate regression metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print regression metrics
print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Coefficient of Determination (R^2): {r2}')

# Get the coefficients
coefficients = best_ridge_model.coef_

# Get the absolute magnitude of coefficients
abs_coefficients = abs(coefficients)

# Get indices of top 10 features
top_10_indices = abs_coefficients.argsort()[-10:][::-1]

# Get feature names
feature_names = X.columns  # Assuming X is a pandas DataFrame containing the features

# Print the top 10 most important features
print()
print("Top 10 Most Important Features:")
for index in top_10_indices:
    print(f'{feature_names[index]}: {coefficients[index]}')

model_path = 'melting_point_lr_model.joblib'
joblib.dump({
    'model': best_ridge_model,
    'scaler': scaler,
    'feature_names': FEATURE_NAMES,
    'model_name': 'Ridge Regression',
}, model_path)
print(f"\nSaved best model to {model_path}")
