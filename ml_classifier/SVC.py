import os
import pandas as pd
import numpy as np
import time
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.svm import SVC

# Use SLURM environment variables for CPU count
num_cpus = int(os.getenv('SLURM_CPUS_PER_TASK', 1))
random_seed = 0

def load_and_prepare_data(pos_file, neg_file):
    pos_df = pd.read_csv(pos_file, sep='\t').drop(columns=['SMILES'], errors='ignore').dropna()
    neg_df = pd.read_csv(neg_file, sep='\t').drop(columns=['SMILES'], errors='ignore').dropna()
    
    pos_df['label'] = 1
    neg_df['label'] = 0
    
    data = pd.concat([pos_df, neg_df], axis=0).sample(frac=1, random_state=random_seed).reset_index(drop=True)
    X, y = data.iloc[:, :-1], data['label']
    
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, stratify=y, random_state=random_seed)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=random_seed)
    
    return (X_train, X_val, X_test, y_train, y_val, y_test), X.columns

def train_and_evaluate(X_train, X_val, X_test, y_train, y_val, y_test):
    scaler = StandardScaler().fit(X_train)
    X_train, X_val, X_test = scaler.transform(X_train), scaler.transform(X_val), scaler.transform(X_test)
    
    model = SVC(C=1, kernel='rbf', gamma='scale', class_weight='balanced', random_state=random_seed)
    
    start_time = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start_time
    
    results = []
    for dataset, X, y in [('Train', X_train, y_train), ('Validation', X_val, y_val), ('Test', X_test, y_test)]:
        y_pred = model.predict(X)
        report = classification_report(y, y_pred, output_dict=True)
        results.append(['SVM', dataset, accuracy_score(y, y_pred), report['1']['precision'], 
                        report['1']['recall'], report['1']['f1-score'], training_time])
    
    return pd.DataFrame(results, columns=['Model', 'Dataset', 'Accuracy', 'Precision (Positive)', 
                                          'Recall (Positive)', 'F1-Score (Positive)', 'Training Time (s)']), scaler, model

def evaluate_secondary_test(model, scaler, test_file, feature_names):
    test_df = pd.read_csv(test_file, sep='\t')
    X_test = test_df[feature_names]  # Ensure alignment by selecting the same columns
    X_test = scaler.transform(X_test)
    y_true = test_df['IsNatural'].values.flatten().tolist()
    
    y_pred = model.predict(X_test)
    report = classification_report(y_true, y_pred, output_dict=True)
    results = [['SVC', 'Secondary Test', accuracy_score(y_true, y_pred), report['1']['precision'], report['1']['recall'], report['1']['f1-score']]]

    return pd.DataFrame(results, columns=['Model', 'Dataset', 'Accuracy', 'Precision (Positive)', 'Recall (Positive)', 'F1-Score (Positive)'])

if __name__ == '__main__':
    pos_file = 'positive_training.csv'
    neg_file = 'negative_training.csv'
    secondary_test_file = 'testset.csv'
    
    (X_train, X_val, X_test, y_train, y_val, y_test), feature_names = load_and_prepare_data(pos_file, neg_file)
    results, scaler, model = train_and_evaluate(X_train, X_val, X_test, y_train, y_val, y_test)
    
    print("Classifier Performance on Training, Validation, and Test Sets")
    print(results.to_string(index=False, float_format='%.2f'))
    
    secondary_results = evaluate_secondary_test(model, scaler, secondary_test_file, feature_names)
    print("\nClassifier Performance on Secondary Test Set")
    print(secondary_results.to_string(index=False, float_format='%.2f'))

    model_path = 'svc_model.joblib'
    joblib.dump({
        'model': model,
        'scaler': scaler,
        'feature_names': list(feature_names),
        'model_name': 'SVC',
    }, model_path)
    print(f"\nSaved best model to {model_path}")
