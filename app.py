import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# -------------------------
# Load trained model
# -------------------------
model_path = r"E:\Major Project\random_forest_model.pkl"  # change path if needed

with open(model_path, "rb") as file:
    regressor = pickle.load(file)

# -------------------------
# Vegetable mapping
# -------------------------
vegetable_mapping = {
    'Tomato': 1,
    'Potato': 2,
    'Onion': 3,
    'Cabbage': 4,
    'Cauliflower': 5,
}

# -------------------------
# Season mapping function
# -------------------------
def get_season_from_month(month):
    if month in [1, 2, 11, 12]:
        return 1  # Winter
    elif month in [3, 4, 5, 6]:
        return 2  # Summer
    elif month in [7, 8, 9, 10]:
        return 3  # Monsoon
    else:
        return 0  # Unknown

# -------------------------
# Streamlit UI
# -------------------------
st.title("🥦 Vegetable Price Prediction App")

# Sidebar inputs
st.sidebar.header("User Inputs")

veg_name = st.sidebar.selectbox("Select Vegetable", list(vegetable_mapping.keys()))
date_input = st.sidebar.date_input("Select Date", datetime.today())
festival = st.sidebar.radio("Festival?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
rainfall = st.sidebar.number_input("Rainfall Amount (mm)", min_value=0.0, value=0.0, step=0.1)
avg_prev5 = st.sidebar.number_input("Average Price of Previous 5 Days", min_value=0.0, value=10.0, step=0.1)
arrival = st.sidebar.number_input("Arrival Amount (tons)", min_value=0.0, value=1.0, step=0.1)

# -------------------------
# Convert inputs
# -------------------------
vegetable = vegetable_mapping[veg_name]
day = date_input.day
month = date_input.month
season = get_season_from_month(month)

user_input = np.array([day, vegetable, festival, rainfall, season, avg_prev5, arrival]).reshape(1, -1)

# -------------------------
# Prediction
# -------------------------
if st.sidebar.button("Predict Price"):
    predicted_price = regressor.predict(user_input)
    st.success(f"💰 Predicted Price for {veg_name} on {date_input} is: **{predicted_price[0]:.2f}**")
