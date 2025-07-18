# Gender -> 1:Female 0:Male
# Churn -> 1:Yes 0:No
# Scaler is exported as scaler.pkl
# Model is exported as Model.pkl
# Order of X is ['Age', 'Gender', 'Tenure', 'MonthlyCharges']

import streamlit as st
import joblib 
import numpy as np

#Loading scaler and model
scaler = joblib.load("scaler.pkl")
model = joblib.load("Model.pkl")


st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and click the Prediction Button for Prediction")

st.divider()

#Taking Inputs

age = st.number_input("Enter age", min_value=10, max_value=100, value=30)
gender = st.selectbox("Enter the Gender", ["Male", "Female"])
tenure = st.number_input("Enter Tenure:", min_value=0, max_value=130, value=10)
monthlycharge = st.number_input("Enter Montly Charge", min_value=30, max_value=150)

st.divider()

predictbutton = st.button("Predict!")

if predictbutton:

    gender_selected = 1 if gender == "Female" else 0

    X = [age, gender_selected, tenure, monthlycharge]

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    predicted = "Churn" if prediction == 1 else "Not Churn"

    st.write(f"Predicted: {predicted}")


else:
    st.write("Please enter the values and use predict button")























