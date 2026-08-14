import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
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


# Train a Random Forest Regressor model
rf_regressor = RandomForestRegressor(random_state=42)

# Perform GridSearchCV for hyperparameter tuning
param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20], 'min_samples_split': [2, 5, 10]}
grid_search = GridSearchCV(rf_regressor, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train_scaled, y_train)

# Get the best model from the grid search
best_rf_model = grid_search.best_estimator_

# Print the optimal hyperparameters
print("Optimal Hyperparameters:")
print(grid_search.best_params_)

# Make predictions on the test set
y_pred = best_rf_model.predict(X_test_scaled)

fhout=open('predicted_melting_points_rf.csv', 'w')
# Write predicted melting points to a file                                                                                                                   
fhout.write('SMILES' + ',' + 'Target_MP' + ',' + 'Predicted_MP' + '\n')

for (smi, y_t, y_p) in zip(data.loc[y_test.index, 'smiles'], y_test, y_pred):
    fhout.write(str(smi) + ',' + str(y_t) + ',' + str(y_p) + '\n')
fhout.close()

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Coefficient of Determination (R^2): {r2}')

feature_importances = best_rf_model.feature_importances_

# Get indices of top 10 most important features
top_indices = feature_importances.argsort()[-10:][::-1]

# Get the names of the top features
top_features = X_train.columns[top_indices]

# Print the top features
print('\n')
print("Random forest model")
print("Top 10 Most Important Features:")
for feature in top_features:
    print(feature)

model_path = 'melting_point_rf_model.joblib'
joblib.dump({
    'model': best_rf_model,
    'scaler': scaler,
    'feature_names': FEATURE_NAMES,
    'model_name': 'Random Forest Regressor',
}, model_path)
print(f"\nSaved best model to {model_path}")
