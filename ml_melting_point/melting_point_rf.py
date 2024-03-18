import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

# Function to calculate molecular descriptors
def calculate_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        descriptors = [
            Descriptors.NHOHCount(mol), Descriptors.NOCount(mol),
            Descriptors.NumAliphaticCarbocycles(mol), Descriptors.NumAliphaticHeterocycles(mol),
            Descriptors.NumAliphaticRings(mol), Descriptors.NumAromaticCarbocycles(mol),
            Descriptors.NumAromaticHeterocycles(mol), Descriptors.NumAromaticRings(mol),
            Descriptors.NumHAcceptors(mol), Descriptors.NumHDonors(mol),
            Descriptors.NumHeteroatoms(mol), Descriptors.NumRadicalElectrons(mol),
            Descriptors.NumRotatableBonds(mol), Descriptors.NumSaturatedCarbocycles(mol),
            Descriptors.NumSaturatedHeterocycles(mol), Descriptors.NumSaturatedRings(mol),
            Descriptors.NumValenceElectrons(mol), Descriptors.qed(mol),
            Descriptors.TPSA(mol), Descriptors.MolMR(mol), Descriptors.BalabanJ(mol),
            Descriptors.BertzCT(mol), Descriptors.fr_Al_OH(mol), Descriptors.fr_Al_OH_noTert(mol),
            Descriptors.fr_ArN(mol), Descriptors.fr_Ar_COO(mol), Descriptors.fr_ArN(mol),
            Descriptors.fr_Ar_NH(mol), Descriptors.fr_Ar_OH(mol), Descriptors.fr_COO(mol),
            Descriptors.fr_COO2(mol), Descriptors.fr_C_O(mol), Descriptors.fr_C_O_noCOO(mol),
            Descriptors.fr_C_S(mol), Descriptors.fr_HOCCN(mol), Descriptors.fr_Imine(mol),
            Descriptors.fr_NH0(mol), Descriptors.fr_NH1(mol), Descriptors.fr_NH2(mol),
            Descriptors.fr_N_O(mol), Descriptors.fr_Ndealkylation1(mol),
            Descriptors.fr_Ndealkylation2(mol), Descriptors.fr_Nhpyrrole(mol),
            Descriptors.fr_SH(mol), Descriptors.fr_aldehyde(mol),
            Descriptors.fr_alkyl_carbamate(mol), Descriptors.fr_alkyl_halide(mol),
            Descriptors.fr_allylic_oxid(mol), Descriptors.fr_amide(mol),
            Descriptors.fr_amidine(mol), Descriptors.fr_aniline(mol),
            Descriptors.fr_aryl_methyl(mol), Descriptors.fr_azide(mol),
            Descriptors.fr_azo(mol), Descriptors.fr_barbitur(mol),
            Descriptors.fr_benzene(mol), Descriptors.fr_benzodiazepine(mol),
            Descriptors.fr_bicyclic(mol), Descriptors.fr_diazo(mol),
            Descriptors.fr_dihydropyridine(mol), Descriptors.fr_epoxide(mol),
            Descriptors.fr_ester(mol), Descriptors.fr_ether(mol),
            Descriptors.fr_furan(mol), Descriptors.fr_guanido(mol),
            Descriptors.fr_halogen(mol), Descriptors.fr_hdrzine(mol),
            Descriptors.fr_hdrzone(mol), Descriptors.fr_imidazole(mol),
            Descriptors.fr_imide(mol), Descriptors.fr_isocyan(mol),
            Descriptors.fr_isothiocyan(mol), Descriptors.fr_ketone(mol),
            Descriptors.fr_ketone_Topliss(mol), Descriptors.fr_lactam(mol),
            Descriptors.fr_lactone(mol), Descriptors.fr_methoxy(mol),
            Descriptors.fr_morpholine(mol), Descriptors.fr_nitrile(mol),
            Descriptors.fr_nitro(mol),
            Descriptors.fr_nitro_arom_nonortho(mol), Descriptors.fr_nitroso(mol),
            Descriptors.fr_oxazole(mol), Descriptors.fr_oxime(mol),
            Descriptors.fr_para_hydroxylation(mol), Descriptors.fr_phenol(mol),
            Descriptors.fr_phenol_noOrthoHbond(mol), Descriptors.fr_phos_acid(mol),
            Descriptors.fr_phos_ester(mol), Descriptors.fr_piperdine(mol),
            Descriptors.fr_piperzine(mol), Descriptors.fr_priamide(mol),
            Descriptors.fr_prisulfonamd(mol), Descriptors.fr_pyridine(mol),
            Descriptors.fr_quatN(mol), Descriptors.fr_sulfide(mol),
            Descriptors.fr_sulfonamd(mol), Descriptors.fr_sulfone(mol),
            Descriptors.fr_term_acetylene(mol), Descriptors.fr_tetrazole(mol),
            Descriptors.fr_thiazole(mol), Descriptors.fr_thiocyan(mol),
            Descriptors.fr_thiophene(mol), Descriptors.fr_unbrch_alkane(mol),
            Descriptors.fr_urea(mol), Descriptors.MolWt(mol), Descriptors.MolLogP(mol)
        ]
        return descriptors
    else:
        return [None, None, None]

# Load data from CSV file
data = pd.read_csv('melting_points.csv')  # Replace 'training_data.csv' with your actual file

# Generate molecular descriptors from SMILES strings
data['Descriptors'] = data['smiles'].apply(calculate_descriptors)

# Split the data into features and target variable
X = pd.DataFrame(data['Descriptors'].tolist(), columns=[
    'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles',
    'NumAliphaticRings', 'NumAromaticCarbocycles', 'NumAromaticHeterocycles',
    'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms',
    'NumRadicalElectrons', 'NumRotatableBonds', 'NumSaturatedCarbocycles',
    'NumSaturatedHeterocycles', 'NumSaturatedRings', 'NumValenceElectrons',
    'qed', 'TPSA', 'MolMR', 'BalabanJ', 'BertzCT', 'fr_Al_OH', 'fr_Al_OH_noTert',
    'fr_ArN', 'fr_Ar_COO', 'fr_ArN', 'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO',
    'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine',
    'fr_NH0', 'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1',
    'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde',
    'fr_alkyl_carbamate', 'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide',
    'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo',
    'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo',
    'fr_dihydropyridine', 'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan',
    'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole',
    'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss',
    'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile',
    'fr_nitro',  'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole',
    'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond',
    'fr_phos_acid', 'fr_phos_ester', 'fr_piperdine', 'fr_piperzine', 'fr_priamide',
    'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd',
    'fr_sulfone', 'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan',
    'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea', 'MolWt', 'MolLogP'])
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

for (smi, y_t, y_p) in zip(data['smiles'], y_test, y_pred):
    fhout.write(str(smi) + ',' + str(y_t) + ',' + str(y_p) + '\n') 
fhout.close()

mse = mean_squared_error(y_test, y_pred)

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
