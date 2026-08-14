"""Predict whether a molecule is natural (1) or not (0) from a SMILES string, using a model
saved by one of RandomForest.py, LogisticRegression.py, MLP.py, SVC.py or HistGradientBoost.py.

Usage:
    python predict.py --model random_forest_model.joblib --smiles "CC(=O)Oc1ccccc1C(=O)O"
"""

import argparse

import joblib
import pandas as pd

from descriptors import build_feature_vector


def predict(model_path, smiles):
    bundle = joblib.load(model_path)
    model = bundle['model']
    scaler = bundle['scaler']
    feature_names = bundle['feature_names']

    feature_vector = build_feature_vector(smiles, feature_names)
    if feature_vector is None:
        raise ValueError(f"Could not parse SMILES string: {smiles!r}")

    X = pd.DataFrame([feature_vector], columns=feature_names)
    X_scaled = scaler.transform(X)

    label = int(model.predict(X_scaled)[0])
    probability = None
    if hasattr(model, 'predict_proba'):
        probability = float(model.predict_proba(X_scaled)[0][1])

    return bundle.get('model_name', 'model'), label, probability


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict IsNatural (0/1) for a SMILES string from a saved classifier.')
    parser.add_argument('--model', required=True, help='Path to a saved model .joblib file')
    parser.add_argument('--smiles', required=True, help='SMILES string of the molecule')
    args = parser.parse_args()

    model_name, label, probability = predict(args.model, args.smiles)

    print(f"Model: {model_name}")
    print(f"SMILES: {args.smiles}")
    print(f"Predicted label: {label} ({'natural' if label == 1 else 'not natural'})")
    if probability is not None:
        print(f"Predicted probability of natural (label=1): {probability:.4f}")
