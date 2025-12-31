from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# load model
model = pickle.load(open("Linear_RegressionModel.pkl", "rb"))

@app.route('/')
def home():
    return "Car Price Prediction API is running 🚗"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    df = pd.DataFrame([[
        data['name'],
        data['company'],
        int(data['year']),
        int(data['kms_driven']),
        data['fuel_type']
    ]], columns=['name','company','year','kms_driven','fuel_type'])

    prediction = model.predict(df)[0]

    return jsonify({
        "predicted_price": round(prediction, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
