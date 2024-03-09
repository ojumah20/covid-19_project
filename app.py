import streamlit as st
import pickle
import numpy as np

def predict(features):
    # Load the saved model
    with open('xgboost.pkl', 'rb') as f:
        xgb = pickle.load(f)

    # Convert features to a numpy array
    X = np.array([list(features.values())])

    # Make predictions
    predictions = xgb.predict(X)

    return predictions

def main():
    st.title("Lung Cancer Prediction")

    st.write("Enter patient information below:")
    features = {}
    for key in [
        'Patient age quantile', 'Platelets', 'Mean platelet volume',
        'Red blood Cells', 'Lymphocytes', 'Mean corpuscular hemoglobin concentration (MCHC)',
        'Basophils', 'Mean corpuscular hemoglobin (MCH)', 'Eosinophils',
        'Red blood cell distribution width (RDW)', 'CoronavirusNL63',
        'Rhinovirus/Enterovirus', 'Parainfluenza 4', 'Parainfluenza 2',
        'Neutrophils', 'Urea', 'Proteina C reativa mg/dL', 'Creatinine',
        'Potassium', 'Sodium', 'Influenza B, rapid test'
    ]:
        features[key] = st.number_input(key, value=0)

    if st.button("Predict"):
        predictions = predict(features)
        st.write("Predictions:", predictions)

if __name__ == "__main__":
    main()
