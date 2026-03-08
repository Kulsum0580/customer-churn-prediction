import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📡", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"]  { font-family: "Inter", sans-serif; }
.stApp { background-color: #0f172a; color: #e2e8f0; }
section[data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
.churn-card { background: linear-gradient(135deg,#450a0a,#7f1d1d); border: 2px solid #ef4444; border-radius:16px; padding:30px; text-align:center; margin:20px 0; }
.stay-card  { background: linear-gradient(135deg,#052e16,#14532d); border: 2px solid #22c55e; border-radius:16px; padding:30px; text-align:center; margin:20px 0; }
.result-title { font-size:2rem; font-weight:700; margin-bottom:8px; }
.result-sub   { font-size:1rem; opacity:0.8; }
.metric-card  { background:#1e293b; border:1px solid #334155; border-radius:12px; padding:20px; text-align:center; }
.tip-box { background:#1e293b; border-left:3px solid #3b82f6; border-radius:0 8px 8px 0; padding:12px 16px; margin:8px 0; font-size:0.85rem; color:#94a3b8; }
.stButton>button { width:100%; background:linear-gradient(135deg,#3b82f6,#6366f1); color:white; border:none; border-radius:10px; padding:14px 0; font-size:1rem; font-weight:600; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_artifacts():
    with open("customer_churn_model.pkl","rb") as f:
        md = pickle.load(f)
    with open("encoders.pkl","rb") as f:
        enc = pickle.load(f)
    return md["model"], enc

try:
    model, encoders = load_artifacts()
    model_loaded = True
except Exception as e:
    model_loaded = False
    load_error = str(e)

with st.sidebar:
    st.markdown("## Customer Details")

    st.markdown("**Demographics**")
    gender     = st.selectbox("Gender",         ["Female","Male"])
    senior     = st.selectbox("Senior Citizen", [0,1], format_func=lambda x:"Yes" if x==1 else "No")
    partner    = st.selectbox("Partner",        ["Yes","No"])
    dependents = st.selectbox("Dependents",     ["No","Yes"])

    st.markdown("**Account**")
    tenure    = st.slider("Tenure (months)", 0, 72, 12)
    contract  = st.selectbox("Contract", ["Month-to-month","One year","Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes","No"])
    payment   = st.selectbox("Payment Method", ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])

    st.markdown("**Phone**")
    phone_service  = st.selectbox("Phone Service",  ["Yes","No"])
    multiple_lines = st.selectbox("Multiple Lines",  ["No","Yes","No phone service"])

    st.markdown("**Internet**")
    internet_service  = st.selectbox("Internet Service",  ["DSL","Fiber optic","No"])
    online_security   = st.selectbox("Online Security",   ["No","Yes","No internet service"])
    online_backup     = st.selectbox("Online Backup",     ["Yes","No","No internet service"])
    device_protection = st.selectbox("Device Protection", ["No","Yes","No internet service"])
    tech_support      = st.selectbox("Tech Support",      ["No","Yes","No internet service"])
    streaming_tv      = st.selectbox("Streaming TV",      ["No","Yes","No internet service"])
    streaming_movies  = st.selectbox("Streaming Movies",  ["No","Yes","No internet service"])

    st.markdown("**Billing**")
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 29.85, step=0.01)
    total_charges   = st.number_input("Total Charges ($)",   0.0, 10000.0, float(tenure * monthly_charges), step=0.01)

    predict_btn = st.button("Predict Churn")

st.markdown("# Customer Churn Predictor")
st.markdown("Predict whether a telecom customer will churn using a trained **Random Forest** model.")

if not model_loaded:
    st.error(f"Could not load model: {load_error}")
    st.stop()

if predict_btn:
    input_data = {
        "gender": gender, "SeniorCitizen": senior, "Partner": partner,
        "Dependents": dependents, "tenure": tenure, "PhoneService": phone_service,
        "MultipleLines": multiple_lines, "InternetService": internet_service,
        "OnlineSecurity": online_security, "OnlineBackup": online_backup,
        "DeviceProtection": device_protection, "TechSupport": tech_support,
        "StreamingTV": streaming_tv, "StreamingMovies": streaming_movies,
        "Contract": contract, "PaperlessBilling": paperless,
        "PaymentMethod": payment, "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }

    df = pd.DataFrame([input_data])
    for col, enc in encoders.items():
        df[col] = enc.transform(df[col])

    pred      = model.predict(df)[0]
    prob      = model.predict_proba(df)[0]
    churn_pct = prob[1] * 100
    stay_pct  = prob[0] * 100

    _, mid, _ = st.columns([1,2,1])
    with mid:
        if pred == 1:
            st.markdown(f'<div class="churn-card"><div class="result-title">Warning: Likely to Churn</div><div class="result-sub">Churn probability: <strong>{churn_pct:.1f}%</strong></div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="stay-card"><div class="result-title">Likely to Stay</div><div class="result-sub">Retention probability: <strong>{stay_pct:.1f}%</strong></div></div>', unsafe_allow_html=True)

    st.markdown("### Probability Breakdown")
    c1, c2 = st.columns(2)
    c1.metric("Churn Probability",     f"{churn_pct:.1f}%")
    c2.metric("Retention Probability", f"{stay_pct:.1f}%")
    st.progress(int(churn_pct))

    st.markdown("### Retention Tips")
    if contract == "Month-to-month":
        st.markdown('<div class="tip-box">Month-to-month contract - offer a discounted annual plan.</div>', unsafe_allow_html=True)
    if tenure < 12:
        st.markdown('<div class="tip-box">Tenure under 1 year - early engagement is critical.</div>', unsafe_allow_html=True)
    if internet_service == "Fiber optic" and online_security == "No":
        st.markdown('<div class="tip-box">Fiber optic without security - bundle add-ons at a discount.</div>', unsafe_allow_html=True)
    if payment == "Electronic check":
        st.markdown('<div class="tip-box">Electronic check users churn more - encourage auto-pay.</div>', unsafe_allow_html=True)

    with st.expander("View Input Summary"):
        summary = pd.DataFrame(list(input_data.items()), columns=["Feature","Value"])
        st.dataframe(summary, use_container_width=True, hide_index=True)

else:
    st.info("Fill in customer details in the sidebar and click Predict Churn.")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-card"><h3>Random Forest</h3><p>Model Type</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card"><h3>~78%</h3><p>Test Accuracy</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><h3>19</h3><p>Features Used</p></div>', unsafe_allow_html=True)
