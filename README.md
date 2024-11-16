
# Air Quality Prediction

This repository contains a Flask-based web application for predicting air quality of Lucknow city using regression technique named Random Forest. The application utilizes advanced machine learning models and a comprehensive dataset to analyze and predict air quality metrics.

---

## Features

- **Predictive Models**: Utilizes Random Forest regression technique for air quality prediction.
- **Data Insights**: Provides visualizations of air quality trends using Matplotlib and Seaborn.
- **Interactive Web App**: Flask-based interface for users to input data and view predictions.
- **Location-Specific Analysis**: Includes datasets of Lucknow cities to provide accurate local insights.

---

## Tech Stack

- **Frontend**: HTML, JavaScript
- **Backend**: Flask
- **Libraries/Frameworks**:
  - **Machine Learning**: Scikit-learn
  - **Data Manipulation**: Pandas, NumPy
  - **Visualization**: Matplotlib, Seaborn
  - **Statistical Analysis**: SciPy
- **Deployment**: Cloud computing platforms (e.g., AWS, Google Cloud)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/air_quality_prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd air_quality_prediction
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Install the frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```
5. Start the Flask server:
   ```bash
   python app.py
   ```
6. Start the React frontend:
   ```bash
   cd frontend
   npm start
   ```

---

## Dataset

- **Sources**:  
  - Air pollutant gases dataset (Lucknow City) : **23000 records** 
- **Format**: CSV files  
- **Attributes**: Includes pollutant concentrations, date-time, and location data.

---

## Usage

1. Open the web application in your browser (usually at `http://127.0.0.1:5000`).
2. Input location-specific air quality data or parameters.
3. View the predicted air quality index (AQI) and associated visualizations.

---

## Evaluation Metrics

The models are evaluated using:
- **Mean Absolute Error (MAE)**
- **R2 Score**

---

## Visualizations

The project provides the following visualizations:
- Trends of air pollutant concentrations over time.
- Heatmaps for spatial distribution of pollutants.
- Model performance comparisons.

---

## Future Enhancements

- Integration of **Google Maps** for interactive location selection.
- Real-time AQI updates using external APIs.
- Support for additional cities and datasets.

---

## Contributors

- [Sweta Singh](https://github.com/swetasingh8844) - Developer and Researcher  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---
