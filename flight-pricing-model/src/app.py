import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
import sklearn

def preprocess_input(user_input, model_columns):
    df = pd.DataFrame([user_input])
    df = pd.get_dummies(df)

    # Align columns with training data
    df = df.reindex(columns=model_columns, fill_value=0)
    return df

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "linear_regression.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

model_columns = model.feature_names_in_

st.title("Flight Price Predictor")
st.write("Predict flight prices based on route, airline, and travel details.")

airline = st.selectbox("Airline", ["SpiceJet", "Indigo", "Air_India", "Vistara", "AirAsia", "GO_FIRST"])
source_city = st.selectbox("Source City", ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"])
destination_city = st.selectbox("Destination City", ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"])
departure_time = st.selectbox("Departure Time", ["Early_Morning", "Morning", "Afternoon", "Evening", "Night", "Late_Night"])
arrival_time = st.selectbox("Arrival Time", ["Morning", "Afternoon", "Evening", "Night", "Late_Night"])
flight_class = st.selectbox("Class", ["Economy", "Business"])
stops = st.selectbox("Stops", ["zero", "one", "two", "three"])
duration = st.slider("Duration (hours)", 1.0, 10.0, 2.0)
days_left = st.slider("Days to Departure", 1, 60, 15)

stops_map = {"zero": 0, "one": 1, "two": 2, "three": 3}

user_input = {
    "airline": airline,
    "source_city": source_city,
    "destination_city": destination_city,
    "departure_time": departure_time,
    "arrival_time": arrival_time,
    "class": flight_class,
    "stops": stops_map[stops],
    "duration": duration,
    "days_left": days_left
}

if st.button("Predict Price"):
    X_user = preprocess_input(user_input, model_columns)
    prediction = model.predict(X_user)[0]

    st.success(f"💰 Estimated Price: ₹{int(prediction):,}")