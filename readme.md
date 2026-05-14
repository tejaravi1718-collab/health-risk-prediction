# Smart Health Risk Prediction & Recommendation System

## Project Overview

The Smart Health Risk Prediction & Recommendation System is a Machine Learning-based healthcare application designed to predict diabetes risk using patient health and lifestyle information.

The system analyzes various medical and lifestyle parameters such as age, BMI, blood glucose level, HbA1c level, smoking history, hypertension, and heart disease to determine whether a person falls under:

* Low Risk
* Medium Risk
* High Risk

The application also provides personalized health recommendations based on the predicted risk level.

---

# Problem Statement

Healthcare organizations often face challenges in identifying individuals who may develop serious health risks due to lifestyle habits and medical conditions.

This project aims to build an intelligent healthcare prediction system that:

* predicts diabetes risk,
* analyzes patient health data,
* and provides preventive health recommendations.

---

# Features

* Diabetes Risk Prediction
* Risk Categorization (Low / Medium / High)
* Personalized Health Recommendations
* Exploratory Data Analysis (EDA)
* Multiple Machine Learning Models
* Model Performance Comparison
* Streamlit Web Application
* Interactive User Interface

---

# Dataset

Dataset used:

* Diabetes Prediction Dataset from Kaggle

Features used:

* Gender
* Age
* Hypertension
* Heart Disease
* Smoking History
* BMI
* HbA1c Level
* Blood Glucose Level

Target Variable:

* Diabetes (0 = No Diabetes, 1 = Diabetes)

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Streamlit
* Joblib

---

# Machine Learning Workflow

## 1. Data Collection & Cleaning

* Loaded healthcare dataset
* Removed duplicate records
* Encoded categorical features
* Prepared data for ML models

## 2. Exploratory Data Analysis (EDA)

Performed:

* Diabetes distribution analysis
* Age vs diabetes analysis
* BMI analysis
* Correlation heatmap
* Blood glucose analysis
* HbA1c analysis
* Lifestyle comparison charts

## 3. Model Building

Implemented and compared:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

## 4. Model Evaluation

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

# Model Performance Comparison

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.96     | 0.87      | 0.64   | 0.74     |
| Decision Tree       | 0.95     | 0.69      | 0.73   | 0.71     |
| Random Forest       | 0.97     | 0.95      | 0.69   | 0.80     |
| XGBoost             | 0.97     | 0.99      | 0.69   | 0.81     |

---

# Best Model Selection

XGBoost was selected as the final model because it achieved:

* highest F1-score,
* excellent precision,
* strong overall performance on imbalanced healthcare data.

The model effectively captured nonlinear relationships between health features and diabetes risk.

---

# Recommendation System

The application generates personalized recommendations based on:

* predicted risk level,
* BMI,
* blood glucose level,
* smoking habits,
* lifestyle conditions.

Example recommendations:

* Reduce sugar intake
* Increase physical activity
* Monitor blood glucose regularly
* Weight management suggestions
* Smoking cessation advice

---

# Streamlit Web Application

The project includes an interactive Streamlit dashboard where users can:

* enter health details,
* predict diabetes risk,
* view probability scores,
* receive health recommendations.

---

# Project Structure

```plaintext
health-risk-prediction/

│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── xgboost_model.pkl
│   ├── feature_columns.pkl
│
├── notebooks/
│   └── diabetes_prediction.ipynb
```

---

# How to Run the Project

## Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2 — Run Streamlit App

```bash
streamlit run app.py
```

---

# Future Improvements

Possible future enhancements:

* SHAP Explainable AI
* PDF Health Report Generation
* AI Chatbot Integration
* Cloud Deployment
* REST API Development
* Real-Time Health Tracking

---

# Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow including:

* data preprocessing,
* exploratory data analysis,
* model building,
* evaluation,
* deployment,
* and healthcare recommendation generation.

The system provides an intelligent and practical approach for early diabetes risk assessment and preventive healthcare support.
