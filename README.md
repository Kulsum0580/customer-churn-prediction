# 📡 Customer Churn Prediction App

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

> A machine learning web app that predicts whether a telecom customer will churn, built with Random Forest and deployed on Streamlit.

---

## 🚀 Live Demo
👉 **[Click here to open the app]https://customer-churn-prediction-nd8rmh25com2szccvg7lnq.streamlit.app/

---

## 📌 What this project does
- Analyzes 7000+ telecom customer records
- Compares Decision Tree, Random Forest and XGBoost models
- Deploys a real-time prediction app where you enter customer details and get instant churn prediction

---

## 🧠 Best Model — Random Forest
| Metric | Score |
|---|---|
| Accuracy | 77.6% |
| Recall (Churn) | 70% |
| F1-Score (Churn) | 62% |

---

## 📊 Top Churn Factors
| Feature | Impact |
|---|---|
| Contract Type | Highest |
| Online Security | High |
| Tenure | High |
| Tech Support | High |
| Monthly Charges | Medium |

---

## 🛠️ Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, XGBoost, SHAP
- SMOTE for class imbalance
- Streamlit for deployment

---

## ▶️ Run Locally
bash
pip install -r requirements.txt
streamlit run app.py


---

## 📁 Dataset
[IBM Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
```

