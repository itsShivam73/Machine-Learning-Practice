import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("Linear_RegressionModel.pkl", "rb"))

df = pd.read_csv("quikr_car.csv")
car_company_map = dict(zip(df['name'], df['company']))

st.title("🚗 Car Price Prediction")

name = st.selectbox("Car Name", sorted(car_company_map.keys()))
company = car_company_map[name]
st.text_input("Company", company, disabled=True)

year = st.selectbox("Year", list(range(2000, 2026))[::-1])
kms = st.slider("KMs Driven", 0, 300000, 120, step=1000)
fuel = st.selectbox("Fuel Type", sorted(df['fuel_type'].unique()))

if st.button("Predict"):
    df_input = pd.DataFrame([[name, company, year, kms, fuel]],
        columns=['name','company','year','kms_driven','fuel_type'])

    price = model.predict(df_input)[0]
    st.success(f"Predicted Price: ₹ {round(price,2)}")
