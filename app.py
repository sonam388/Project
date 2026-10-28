import streamlit as st
import joblib

model = joblib.load("model.joblib")


st.title("Student Markrs Predictor")

hours = st.number_input("Enter Study Hours")

if st.button("Click Me"):
    predict = model.predict([[hours]])
    st.success(f"Predicted Makrs : {predict}" )

