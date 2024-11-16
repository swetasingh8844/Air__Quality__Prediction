from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
import pandas as pd
import csv
from datetime import datetime

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('air.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Define feature names
        feature_names = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
        
        # Extract data from form
        feature_values = [float(request.form.get(feature)) for feature in feature_names]
        city = "Lucknow"
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # with open('air.csv', 'a', newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(feature_values)
        # Convert input to DataFrame with feature names
        features_df = pd.DataFrame([feature_values], columns=feature_names)
        
        # Standardize input
        features_scaled = scaler.transform(features_df)
        
        # Predict AQI
        prediction = model.predict(features_scaled)[0]
        
        # Categorize AQI
        if prediction <= 50:
            category = "Good"
            message = "Air quality is considered satisfactory, and air pollution poses little or no risk."
            aqi_bucket = "Good"
        elif prediction <= 100:
            category = "Moderate"
            message = "Air quality is acceptable; however, some pollutants may pose a moderate health concern."
            aqi_bucket = "Moderate"
        elif prediction <= 150:
            category = "Unhealthy for Sensitive Groups"
            message = "Members of sensitive groups may experience health effects."
            aqi_bucket = "Unhealthy for Sensitive Groups"
        elif prediction <= 200:
            category = "Unhealthy"
            message = "Everyone may begin to experience health effects."
            aqi_bucket = "Unhealthy"
        elif prediction <= 300:
            category = "Very Unhealthy"
            message = "Health alert: everyone may experience more serious health effects."
            aqi_bucket = "Very Unhealthy"
        else:
            category = "Hazardous"
            message = "Health warning of emergency conditions."
            aqi_bucket = "Hazardous"
        with open('air.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            
            writer.writerow([city, date] + feature_values + [prediction, aqi_bucket])
        return render_template(
            'air.html',
            prediction_text=f"AQI Prediction: {prediction:.2f}",
            category=f"Category: {category}",
            message=message
        )
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
