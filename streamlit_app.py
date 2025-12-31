import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("Linear_RegressionModel.pkl", "rb"))

st.title("🚗 Car Price Prediction App")

# Dropdown options (you can expand later)
car_names = [
    "Maruti Suzuki Swift",
    "Maruti Suzuki Alto",
    "Hyundai i20",
    "Hyundai Creta",
    "Honda City",
    "Toyota Innova"
]

companies = ["Hyundai", "Mahindra", "Ford", "Maruti", "Skoda", "Audi", "Toyota",
 "Renault", "Honda", "Datsun", "Mitsubishi", "Tata", "Volkswagen",
 "Chevrolet", "Mini", "BMW", "Nissan", "Hindustan", "Fiat", "Force",
 "Mercedes", "Land", "Jaguar", "Jeep", "Volvo"]


fuel_types = ["Petrol", "Diesel", "CNG"]

# Inputs
name = st.selectbox("Car Name", car_names)
company = st.selectbox("Company", companies)
year = st.selectbox("Year", list(range(2000, 2026))[::-1])
kms = st.slider("KMs Driven", 0, 300000, 120, step=1000)
fuel = st.selectbox("Fuel Type", fuel_types)

# Prediction
if st.button("Predict Price"):
    df = pd.DataFrame([[name, company, year, kms, fuel]],
        columns=['name','company','year','kms_driven','fuel_type'])

    price = model.predict(df)[0]
    st.success(f"Predicted Price: ₹ {round(price, 2)}")
