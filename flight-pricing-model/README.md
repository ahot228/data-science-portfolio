# Dynamic Flight Model Simulation

## Overview
This project implements a Dynamic Flight Pricing Model using machine learning techniques. It predicts flight prices based on factors such as airline, source, destination and departure time. The solution includes data processing, model building, visualisation, and deployment.

## Tech Stack
- Python 3.x 
- SQLite (Database)
- Streamlit (Web App Deployment)
- Tableau (Data Visualisation)
- Libraries: pandas, numpy, seaborn, matplotlib

## Structure
```
src/
├── analysis.py
├── app.py
├── load_data.py
├── ddl_scripts.sql
notebooks/
├── linear_regression.pkl
data/
├── flight_price.csv
database/
├── flight_pricing.db
tableau/
├── flight_pricing_dashboard.twb_
README.md
requirements.txt
```

## Steps Implemented
1. Data Collection

- Download dataset from https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction.
- Save as data/flight_price.csv.

2. Database Setup (SQLite)

- Create flight_pricing.db and tables for flights and bookings.

3. Data Loading & Cleaning

- Load CSV into SQLite.
- Handle missing values and encode categorical features.

4. Feature Engineering

- Calculate days_to_departure and peak_season_flag.

5. Exploratory Data Analysis (EDA)

- Visualise price trends using Matplotlib & Seaborn.

6. Model Building

- Train a Linear Regression model.
- Evaluate using RMSE and R².

7. Deployment with Streamlit

- Build an interactive web app for predictions.

8. Tableau Dashboard

- Visualise price trends and route analysis.

## How to Use


1. Clone the repository:

git clone https://github.com/ahot228/data-science-portfolio
cd flight_pricing_model



2. Install dependencies:

pip install -r requirements.txt

3. Run Streamlit app:

streamlit run python/app.py

## Tableau

Visualisations:
- Line Chart: Price vs Days to Departure
- Heatmap: Source-Destination routes
- Gant Bar Chart: Price per class
- Table: Stops vs Price

![Tableau Dashboard](visuals/dashboard.png)
