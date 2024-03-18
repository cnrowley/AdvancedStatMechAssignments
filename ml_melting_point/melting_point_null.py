import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load data from CSV file
data = pd.read_csv('melting_points.csv')  # Replace 'melting_points.csv' with your actual file

# Extract the target variable
y_true = data['mp']

# Calculate the mean and median of the target variable
mean_mp = y_true.mean()

# Predictions using mean and median values
y_pred = [mean_mp] * len(y_true)

fhout=open('predicted_melting_points_null.csv', 'w')
# Write predicted melting points to a file                                                                                                                   
fhout.write('SMILES' + ',' + 'Target_MP' + ',' + 'Predicted_MP' + '\n')

for (smi, y_t, y_p) in zip(data['smiles'], y_true, y_pred):
    fhout.write(str(smi) + ',' + str(y_t) + ',' + str(y_p) + '\n') 
fhout.close()

# Calculate evaluation metrics
mse_mean = mean_squared_error(y_true, y_pred)
mae_mean = mean_absolute_error(y_true, y_pred)
r2_mean = r2_score(y_true, y_pred)

# Print evaluation metrics
print("Null Model using Mean:")
print(f'Mean Squared Error (MSE): {mse_mean}')
print(f'Mean Absolute Error (MAE): {mae_mean}')
print(f'Coefficient of Determination (R^2): {r2_mean}')

