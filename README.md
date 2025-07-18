# Customer Churn Prediction App

A machine learning web app that predicts whether a customer will churn based on demographic and usage features.

## 🔍 Project Overview
- Predicts churn using logistic regression with ~81% accuracy.
- Features: Age, Gender, Tenure, Monthly Charges
- Built with Python, scikit-learn, Streamlit

## 💡 How It Works
- Model and scaler serialized using Joblib
- Web app built with Streamlit
- Users input values and get real-time predictions

## 🛠️ Tech Stack
- Python, scikit-learn, NumPy
- Streamlit, Joblib

## 📦 Setup Instructions
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

## 📁 Files
- `app.py`: Streamlit app code
- `Model.pkl`: Trained ML model
- `scaler.pkl`: Preprocessing scaler
