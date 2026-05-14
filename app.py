import streamlit as st
import pandas as pd
import joblib

# =========================
# LOAD SAVED FILES
# =========================

model = joblib.load('models/xgboost_model.pkl')

feature_columns = joblib.load('models/feature_columns.pkl')

# =========================
# PAGE TITLE
# =========================

st.title("Smart Health Risk Prediction System")
st.markdown("---")

st.write(
    "Predict diabetes risk based on health and lifestyle information."
)

# =========================
# USER INPUTS
# =========================

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

age = st.slider(
    "Age",
    1, 80, 25
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1]
)

heart_disease = st.selectbox(
    "Heart Disease",
    [0, 1]
)

smoking_history = st.selectbox(
    "Smoking History",
    ["never", "No Info", "current", "former", "ever", "not current"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=100.0,
    value=25.0
)

hba1c = st.number_input(
    "HbA1c Level",
    min_value=3.0,
    max_value=10.0,
    value=5.5
)

blood_glucose = st.number_input(
    "Blood Glucose Level",
    min_value=70,
    max_value=300,
    value=120
)

# =========================
# PREDICTION BUTTON
# =========================

if st.button("Predict Risk"):

    # -------------------------
    # CREATE INPUT DICTIONARY
    # -------------------------

    input_data = {
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'bmi': bmi,
        'HbA1c_level': hba1c,
        'blood_glucose_level': blood_glucose
    }

    # -------------------------
    # GENDER ENCODING
    # -------------------------

    input_data['gender_Male'] = 1 if gender == 'Male' else 0

    input_data['gender_Other'] = 1 if gender == 'Other' else 0

    # -------------------------
    # SMOKING HISTORY ENCODING
    # -------------------------

    smoking_categories = [
        'No Info',
        'current',
        'ever',
        'former',
        'never',
        'not current'
    ]

    for category in smoking_categories:

        column_name = f"smoking_history_{category}"

        input_data[column_name] = (
            1 if smoking_history == category else 0
        )

    # -------------------------
    # CONVERT TO DATAFRAME
    # -------------------------

    input_df = pd.DataFrame([input_data])

    # -------------------------
    # MATCH TRAINING COLUMNS
    # -------------------------

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # -------------------------
    # PREDICTION
    # -------------------------

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    # -------------------------
    # RISK LEVEL LOGIC
    # -------------------------

    if probability < 0.15:
        risk_level = "Low Risk"

    elif probability < 0.40:
        risk_level = "Medium Risk"

    else:
        risk_level = "High Risk"

    # -------------------------
    # DISPLAY RESULTS
    # -------------------------

    st.subheader("Prediction Result")

    st.write(f"Diabetes Probability: {probability * 100:.2f}%")

    st.write(f"Risk Level: {risk_level}")
    st.markdown("---")

    # -------------------------
    # RECOMMENDATIONS
    # -------------------------

    recommendations = []

    if risk_level == "High Risk":

        recommendations.append(
            "Reduce sugar intake and monitor glucose regularly."
        )

        recommendations.append(
            "Exercise daily for at least 30 minutes."
        )

        recommendations.append(
            "Consult a healthcare professional."
        )

    elif risk_level == "Medium Risk":

        recommendations.append(
            "Maintain balanced diet and healthy lifestyle."
        )

        recommendations.append(
            "Increase physical activity."
        )

    else:

        recommendations.append(
            "Maintain your healthy habits."
        )

    if bmi > 30:

        recommendations.append(
            "Weight management is recommended."
        )

    if blood_glucose > 180:

        recommendations.append(
            "Monitor blood glucose levels frequently."
        )

    if smoking_history == "current":

        recommendations.append(
            "Smoking cessation is strongly recommended."
        )

    # -------------------------
    # DISPLAY RECOMMENDATIONS
    # -------------------------

    st.subheader("Health Recommendations")

    for rec in recommendations:

        st.write(f"- {rec}")