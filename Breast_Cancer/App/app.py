import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("../Model/breast_cancer_model.pkl") 

df = pd.read_csv("../dataset/Breast_cancer.csv")  
df = df.drop(columns=['Unnamed: 32', 'id'])

st.title("Breast Cancer Prediction App ")
st.write("Fill in the tumor features to predict whether it is malignant or benign.")

X = df.drop('diagnosis', axis=1)

input_values = []

for col in X.columns:
    value = st.number_input(f"{col}", value=float(X[col].mean()), min_value=0)
    input_values.append(value)

if st.button("Predict"):
    input_array = np.array([input_values])
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        st.error("Prediction: Malignant Cancer")
    else:
        st.success("Prediction: Benign Cancer ")
