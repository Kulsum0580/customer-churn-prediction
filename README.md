# 📡 Customer Churn Prediction App

> A machine learning web app that predicts whether a telecom customer will churn, built with Random Forest and deployed on Streamlit.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-00e5a0?style=for-the-badge)](https://customer-churn-prediction-nd8rmh25com2szccvg7lnq.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)

---

## 📌 What This Project Does

- Analyzes **7,043 telecom customer records** from IBM's Telco dataset
- Compares **Decision Tree**, **Random Forest**, and **XGBoost** models
- Deploys a **real-time prediction app** — enter customer details and get an instant churn prediction
- Uses **SMOTE** to handle class imbalance and **SHAP** for model explainability

---

## 🚀 Live Demo

👉 **[Click here to open the app](https://customer-churn-prediction-nd8rmh25com2szccvg7lnq.streamlit.app/)**

---

## 🔄 ML Pipeline

```mermaid
flowchart LR
    A[📥 Raw Data\nIBM Telco CSV] --> B[🧹 Data Cleaning\nHandle nulls & types]
    B --> C[🔢 Feature Engineering\nEncode categoricals]
    C --> D[⚖️ SMOTE\nBalance classes]
    D --> E[✂️ Train / Test Split\n80% / 20%]
    E --> F[🌲 Random Forest\nDecision Tree\nXGBoost]
    F --> G[📊 Evaluation\nAccuracy · Recall · F1]
    G --> H[💡 SHAP\nExplainability]
    H --> I[🚀 Streamlit App\nLive Prediction]

    style A fill:#1a1a2e,color:#00e5a0,stroke:#00e5a0
    style B fill:#1a1a2e,color:#00b8ff,stroke:#00b8ff
    style C fill:#1a1a2e,color:#00b8ff,stroke:#00b8ff
    style D fill:#1a1a2e,color:#00e5a0,stroke:#00e5a0
    style E fill:#1a1a2e,color:#00b8ff,stroke:#00b8ff
    style F fill:#1a1a2e,color:#ff6b6b,stroke:#ff6b6b
    style G fill:#1a1a2e,color:#00e5a0,stroke:#00e5a0
    style H fill:#1a1a2e,color:#00b8ff,stroke:#00b8ff
    style I fill:#1a1a2e,color:#00e5a0,stroke:#00e5a0
```

---

## 🧠 Best Model — Random Forest

| Metric | Score |
|---|---|
| ✅ Accuracy | **77.6%** |
| 🔁 Recall (Churn) | **70%** |
| 🎯 F1-Score (Churn) | **62%** |

---

## 📊 Top Churn Factors

| # | Feature | Impact |
|---|---|---|
| 1 | Contract Type | 🔴 Highest |
| 2 | Online Security | 🟠 High |
| 3 | Tenure | 🟠 High |
| 4 | Tech Support | 🟠 High |
| 5 | Monthly Charges | 🟡 Medium |

---

## 🔬 Model Comparison

| Model | Accuracy | Recall (Churn) | F1 (Churn) |
|---|---|---|---|
| ✦ **Random Forest** | **77.6%** | **70%** | **62%** |
| XGBoost | 76.1% | 68% | 60% |
| Decision Tree | 72.4% | 63% | 57% |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python, Pandas, NumPy | Data processing |
| Scikit-learn | ML modeling |
| XGBoost | Gradient boosting |
| SHAP | Model explainability |
| SMOTE | Class imbalance handling |
| Streamlit | Web deployment |

---

## ▶️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/customer-churn-prediction
cd customer-churn-prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

---

## 📁 Dataset

[IBM Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
