import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import HistGradientBoostingClassifier

# Use SLURM environment variables to determine the number of CPUs
num_cpus = int(os.getenv('SLURM_CPUS_PER_TASK', default=1))  # Default to 1 if not running in SLURM
random_seed = 0 # replace with your student number

def load_and_prepare_data(pos_file, neg_file):
    pos_df = pd.read_csv(pos_file, sep='\t')
    neg_df = pd.read_csv(neg_file, sep='\t')
    
    pos_df = pos_df.dropna()
    neg_df = neg_df.dropna()

    pos_df['label'] = 1
    neg_df['label'] = 0

    data = pd.concat([pos_df, neg_df], axis=0).sample(frac=1).reset_index(drop=True)
    X = data.iloc[:, 1:-1]  # Skip SMILES and label columns
    y = data['label']

    return train_test_split(X, y, test_size=0.3, random_state=random_seed), X.columns

def train_and_evaluate(X_train, X_val, X_test, y_train, y_val, y_test, feature_names):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    param_grid = {
        'learning_rate': [0.01, 0.1, 0.2],
        'max_iter': [100, 200, 300],
        'max_depth': [3, 5, 10]
    }
    sample_weights = calculate_sample_weights(y_train)
    model = GridSearchCV(HistGradientBoostingClassifier(), param_grid, cv=3, scoring='accuracy')
    
    start_time = time.time()
    model.fit(X_train, y_train, sample_weight=sample_weights)
    training_time = time.time() - start_time

    results = []
    for dataset, X, y in [('Train', X_train, y_train), ('Validation', X_val, y_val), ('Test', X_test, y_test)]:
        y_pred = model.predict(X)
        report = classification_report(y, y_pred, output_dict=True)
        results.append(['Gradient Boosting', dataset, accuracy_score(y, y_pred), report['1']['precision'], report['1']['recall'], report['1']['f1-score'], training_time])

    print(f"Best parameters: {model.best_params_}")

    return pd.DataFrame(results, columns=['Model', 'Dataset', 'Accuracy', 'Precision (Positive)', 'Recall (Positive)', 'F1-Score (Positive)', 'Training Time (s)']), scaler, model

def calculate_sample_weights(y):
    class_counts = np.bincount(y)
    total_samples = len(y)
    class_weights = total_samples / (len(class_counts) * class_counts)
    sample_weights = np.array([class_weights[label] for label in y])
    return sample_weights

def evaluate_secondary_test(model, scaler, test_file, feature_names):
    test_df = pd.read_csv(test_file, sep='\t')
    X_test = test_df[feature_names]  # Ensure alignment by selecting the same columns
    X_test = scaler.transform(X_test)
    y_true = test_df['IsNatural'].values.flatten().tolist()
    
    y_pred = model.predict(X_test)
    report = classification_report(y_true, y_pred, output_dict=True)
    results = [['Gradient Boosting', 'Secondary Test', accuracy_score(y_true, y_pred), report['1']['precision'], report['1']['recall'], report['1']['f1-score']]]

    return pd.DataFrame(results, columns=['Model', 'Dataset', 'Accuracy', 'Precision (Positive)', 'Recall (Positive)', 'F1-Score (Positive)'])

if __name__ == '__main__':
    pos_file = 'positive_training.csv'
    neg_file = 'negative_training.csv'
    secondary_test_file = 'testset.csv'

    (X_train, X_temp, y_train, y_temp), feature_names = load_and_prepare_data(pos_file, neg_file)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=random_seed)

    results, scaler, model = train_and_evaluate(X_train, X_val, X_test, y_train, y_val, y_test, feature_names)

    print("Classifier Performance on Training, Validation, and Test Sets")
    print(results.to_string(index=False, float_format='%.2f'))

    secondary_results = evaluate_secondary_test(model, scaler, secondary_test_file, feature_names)

    print("\nClassifier Performance on Secondary Test Set")
    print(secondary_results.to_string(index=False, float_format='%.2f'))
    
