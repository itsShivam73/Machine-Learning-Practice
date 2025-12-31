import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("Linear_RegressionModel.pkl", "rb"))

st.title("🚗 Car Price Prediction App")

name = st.text_input("Car Name", "Maruti Suzuki Swift")
company = st.text_input("Company", "Maruti")
year = st.number_input("Year", 2000, 2025, 2019)
kms = st.number_input("KMs Driven", 0, 300000, 120)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

if st.button("Predict Price"):
    df = pd.DataFrame([[name, company, year, kms, fuel]],
        columns=['name','company','year','kms_driven','fuel_type'])

    price = model.predict(df)[0]
    st.success(f"Predicted Price: ₹ {round(price, 2)}")
