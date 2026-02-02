# 🔋 Battery Health Predictor

A web application that predicts your phone's battery health and recommends whether to **keep using** your phone, **replace the battery**, or **change your phone**.

## Features

- Predicts battery health percentage based on device usage patterns
- Provides actionable recommendations:
  - **Keep Using** (battery health ≥ 75%)
  - **Replace Battery** (battery health 50-74%)
  - **Change Phone** (battery health < 50%)
- Easy-to-use web interface built with Streamlit

## Input Parameters

The model considers the following factors:
- Device age (months)
- Battery capacity (mAh)
- Average screen-on hours per day
- Charging cycles per week
- Average battery temperature
- Fast charging usage percentage
- Overnight charging frequency
- Gaming hours per week
- Video streaming hours per week
- Background app usage level
- Signal strength
- Charging habit score
- Usage intensity score
- Thermal stress index

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/BatteryHealthApp.git
cd BatteryHealthApp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## Requirements

- Python 3.8+
- streamlit
- pandas
- joblib
- scikit-learn
- xgboost

## Usage

1. Fill in your device information in the sidebar
2. Click the "Predict" button
3. View your predicted battery health and recommendation

## License

MIT License
