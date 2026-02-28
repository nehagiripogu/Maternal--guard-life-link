import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("maternal_risk_model.pkl")

# -----------------------------
# Donor Database
# -----------------------------
donors = pd.DataFrame({
    "Name": ["Asha", "Rahul", "Priya", "Kiran", "Meena", "Arjun", "Divya", "Ravi"],
    "BloodGroup": ["O-", "A+", "B+", "AB+", "O+", "A-", "B-", "O-"],
    "Age": [22, 25, 30, 28, 35, 40, 27, 24],
    "Hemoglobin": [13.5, 11.8, 14.2, 12.9, 13.0, 15.1, 10.5, 14.0],
    "Status": ["Available", "Available", "Unavailable", "Available", "Available", "Available", "Available", "Available"]
})

# -----------------------------
# Recipient Compatibility Logic
# -----------------------------
compatibility = {
    "O-": ["O-"],
    "O+": ["O+", "O-"],
    "A-": ["A-", "O-"],
    "A+": ["A+", "A-", "O+", "O-"],
    "B-": ["B-", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "AB-": ["AB-", "A-", "B-", "O-"],
    "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
}

def find_compatible_donors(patient_blood):
    allowed_groups = compatibility[patient_blood]
    return donors[
        (donors["BloodGroup"].isin(allowed_groups)) &
        (donors["Hemoglobin"] > 12.5) &
        (donors["Age"].between(18, 50)) &
        (donors["Status"] == "Available")
    ]

# -----------------------------
# UI
# -----------------------------
st.title("Maternal-Guard & Life-Link")
st.markdown("### AI-Driven Maternal Risk Monitoring & Emergency Donor Network")

st.subheader("Patient Vitals")

age = st.number_input("Age", 15, 50, 25)
sys_bp = st.number_input("Systolic BP", 80, 200, 120)
dia_bp = st.number_input("Diastolic BP", 50, 130, 80)
bs = st.number_input("Blood Sugar (mmol/L)", 6.0, 20.0, 7.5)
temp = st.number_input("Body Temp (F)", 95.0, 105.0, 98.6)
hr = st.number_input("Heart Rate", 40, 200, 80)
blood = st.selectbox("Blood Group", list(compatibility.keys()))

# -----------------------------
# Show Compatible Donors (Always Filtered)
# -----------------------------
if st.button("Check Compatible Donors"):
    compatible = find_compatible_donors(blood)

    st.subheader(f"Compatible Donors for {blood}")
    st.info("Only medically eligible and blood-compatible donors are shown.")

    if len(compatible) > 0:
        st.dataframe(compatible)
    else:
        st.warning("No compatible eligible donors available.")

# -----------------------------
# Prediction
# -----------------------------
if st.button("Analyze Risk"):

    input_data = pd.DataFrame(
        [[age, sys_bp, dia_bp, bs, temp, hr]],
        columns=["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
    )

    probabilities = model.predict_proba(input_data)[0]
    pred_class = probabilities.argmax()

    # Stricter High Risk Threshold
    if pred_class == 2 and probabilities[2] < 0.85:
        pred_class = 1

    risk_map = {0: "Low", 1: "Mid", 2: "High"}
    risk = risk_map[pred_class]

    st.markdown("## Prediction Result")

    if risk == "Low":
        st.success("Low Risk Detected")
    elif risk == "Mid":
        st.warning("Moderate Risk – Close Monitoring Recommended")
    else:
        st.error("🚨 HIGH RISK DETECTED – Emergency Protocol Activated")

    st.write(f"Confidence: {max(probabilities):.2f}")

    # -----------------------------
    # Feature Importance
    # -----------------------------
    st.subheader("Key Risk Drivers")

    feature_importance = pd.DataFrame({
        "Feature": ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"],
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    fig = plt.figure()
    plt.bar(feature_importance["Feature"], feature_importance["Importance"])
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # -----------------------------
    # Emergency Donor Dispatch (Strict)
    # -----------------------------
    if risk == "High":
        st.subheader("Emergency Donor Dispatch")

        compatible_donors = find_compatible_donors(blood)

        if len(compatible_donors) > 0:
            st.success(f"{len(compatible_donors)} Compatible Donor(s) Found")
            st.dataframe(compatible_donors)
        else:
            st.error("No compatible eligible donors available.")