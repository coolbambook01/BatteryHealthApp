import streamlit as st
import pandas as pd
import joblib

# Compatibility fix for sklearn version mismatch
import sklearn.compose._column_transformer as ct

class _RemainderColsList(list):
    """Compatibility wrapper for sklearn's _RemainderColsList"""
    pass

# Add the compatibility class to sklearn module
if not hasattr(ct, '_RemainderColsList'):
    ct._RemainderColsList = _RemainderColsList

# Also make it available in __main__ for pickle
import sys
sys.modules['__main__']._RemainderColsList = _RemainderColsList

# Load your trained pipeline
pipeline = joblib.load("battery_health_xgb_pipeline_fixed.pkl")

# Page config
st.set_page_config(page_title="Battery Health Predictor", layout="wide")

# Title
st.title("🔋 Battery Health Predictor")
st.markdown("""
Predict your device's current battery health percentage and get recommended action.  
Fill in the device details below and click **Predict**.
""")

# Sidebar for inputs
st.sidebar.header("Device Inputs")

# Collect all user inputs (always visible)
device_age = st.sidebar.number_input("Device age (months)", 0, 120, 24, key="device_age")
battery_capacity = st.sidebar.number_input("Battery capacity (mAh)", 1000, 6000, 4500, key="battery_capacity")
screen_hours = st.sidebar.number_input("Avg screen on hours/day", 0.0, 24.0, 5.0, key="screen_hours")
charging_cycles = st.sidebar.number_input("Avg charging cycles/week", 0, 21, 7, key="charging_cycles")
battery_temp = st.sidebar.number_input("Avg battery temp (°C)", 20, 60, 35, key="battery_temp")
fast_charge = st.sidebar.number_input("Fast charging %", 0, 100, 50, key="fast_charge")
overnight_charge = st.sidebar.number_input("Overnight charging/week", 0, 7, 3, key="overnight_charge")
gaming_hours = st.sidebar.number_input("Gaming hours/week", 0.0, 40.0, 8.0, key="gaming_hours")
video_hours = st.sidebar.number_input("Video streaming hours/week", 0.0, 40.0, 10.0, key="video_hours")
bg_usage = st.sidebar.selectbox("Background app usage", ["low","medium","high"], key="bg_usage")
signal_strength = st.sidebar.selectbox("Signal strength avg", ["poor","average","good"], index=1, key="signal_strength")
charging_score = st.sidebar.number_input("Charging habit score", 0, 100, 70, key="charging_score")
usage_score = st.sidebar.number_input("Usage intensity score", 0, 100, 65, key="usage_score")
thermal_index = st.sidebar.number_input("Thermal stress index", 0, 100, 30, key="thermal_index")

# Button to predict
if st.sidebar.button("Predict", key="predict_button"):
    # Create dataframe from inputs
    input_data = {
        "device_age_months": device_age,
        "battery_capacity_mah": battery_capacity,
        "avg_screen_on_hours_per_day": screen_hours,
        "avg_charging_cycles_per_week": charging_cycles,
        "avg_battery_temp_celsius": battery_temp,
        "fast_charging_usage_percent": fast_charge,
        "overnight_charging_freq_per_week": overnight_charge,
        "gaming_hours_per_week": gaming_hours,
        "video_streaming_hours_per_week": video_hours,
        "background_app_usage_level": bg_usage,
        "signal_strength_avg": signal_strength,
        "charging_habit_score": charging_score,
        "usage_intensity_score": usage_score,
        "thermal_stress_index": thermal_index
    }
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    predicted_health = pipeline.predict(input_df)[0]

    # Rule-based recommended action
    if predicted_health >= 75:
        action = "Keep Using"
        action_color = "success"
    elif predicted_health >= 50:
        action = "Replace Battery"
        action_color = "warning"
    else:
        action = "Change Phone"
        action_color = "error"

    # Display results in columns
    col1, col2 = st.columns(2)
    col1.metric("🔹 Predicted Battery Health (%)", f"{predicted_health:.1f}")
    
    if action_color == "success":
        col2.success(f"⚡ Recommended Action: **{action}**")
    elif action_color == "warning":
        col2.warning(f"⚡ Recommended Action: **{action}**")
    else:
        col2.error(f"⚡ Recommended Action: **{action}**")

    st.markdown("---")
    st.info("💡 Adjust the inputs in the sidebar and click **Predict** again to see new results.")
else:
    st.info("👈 Fill in the inputs in the sidebar and click **Predict** to see the battery health prediction.")
