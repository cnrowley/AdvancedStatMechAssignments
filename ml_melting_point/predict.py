"""Predict a melting point (K) from a SMILES string, using a model saved by
melting_point_lr.py, melting_point_mlp.py or melting_point_rf.py.

Usage:
    python predict.py --model melting_point_rf_model.joblib --smiles "CCO"
"""

import argparse

import joblib
import pandas as pd

from descriptors import calculate_descriptors


def predict(model_path, smiles):
    bundle = joblib.load(model_path)
    model = bundle['model']
    scaler = bundle['scaler']
    feature_names = bundle['feature_names']

    descriptors = calculate_descriptors(smiles)
    if descriptors is None:
        raise ValueError(f"Could not parse SMILES string: {smiles!r}")

    X = pd.DataFrame([descriptors], columns=feature_names)
    X_scaled = scaler.transform(X)

    return bundle.get('model_name', 'model'), float(model.predict(X_scaled)[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict melting point (K) for a SMILES string from a saved regression model.')
    parser.add_argument('--model', required=True, help='Path to a saved model .joblib file')
    parser.add_argument('--smiles', required=True, help='SMILES string of the molecule')
    args = parser.parse_args()

    model_name, mp = predict(args.model, args.smiles)

    print(f"Model: {model_name}")
    print(f"SMILES: {args.smiles}")
    print(f"Predicted melting point: {mp:.2f} K")
