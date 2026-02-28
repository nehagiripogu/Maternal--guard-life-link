# Maternal-Guard & Life-Link

# AI-Driven Maternal Risk Monitoring & Emergency Donor Network
# Datathon 2.0 – Problem Statement 3
(Built according to your implemented model and donor logic requirements Maternal-link problem statement… )

# 1. Vision & Social Context
In rural healthcare systems, the “golden hour” is often lost due to delayed diagnosis and fragmented emergency communication. Maternal-Guard & Life-Link transitions maternal care from reactive to proactive by:
Predicting maternal health risk using Machine Learning
Triggering emergency donor matching instantly
Ensuring only medically eligible and blood-compatible donors are displayed
The objective is to create a digital bridge between healthcare workers and emergency donor networks. 
Maternal-link problem statement…

# 2. System Architecture

The solution is a modular web application consisting of two primary components.
Component A: ML Risk Predictor
Model Used: Random Forest Classifier 
Reason for Selection:
Handles nonlinear relationships in maternal vitals
Stable with minimal preprocessing
Provides feature importance for Explainable AI
Input Features:
Age
Systolic Blood Pressure
Diastolic Blood Pressure
Blood Sugar (mmol/L)
Body Temperature (°F)
Heart Rate

Output:
Risk Category: Low / Mid / High
Confidence Score
Feature Importance Visualization
# Additional Enhancements:
Physiological range validation
High-risk probability threshold tuning to reduce false emergency triggers
Feature importance display to satisfy explainability requirement
Component B: Life-Link Donor Network
Implements strict recipient-based compatibility filtering using:
Blood group compatibility rules
Hemoglobin > 12.5 g/dL
Age between 18–50 years
Status marked as “Available”

# Example Compatibility Logic:

Patient Blood Group	Compatible Donors
O−	O− only
O+	O+, O−
A−	A−, O−
AB+	All blood groups
Emergency dispatch is activated only when the predicted risk level is High.
This fulfills the SOS and Donor Dispatch requirement.
Maternal-link problem statement…

# 3. Emergency Workflow

Healthcare worker enters patient vitals
Model predicts risk level
If risk is High:
Emergency protocol activates
Compatible donors are filtered
Eligible donors are displayed
This ensures rapid donor identification during postpartum hemorrhage situations.

# 4. Model Performance

Accuracy: ~75%
F1 Score (High Risk Class): ~0.84
Most Influential Feature: Blood Sugar
Feature importance is visualized in the dashboard to meet explainability requirements.

# 5. Blood Donation Compatibility (Red Blood Cells)

Donor → Recipient Compatibility:
Donor	Can Donate To
O−	All groups
O+	O+, A+, B+, AB+
A−	A−, A+, AB−, AB+
A+	A+, AB+
B−	B−, B+, AB−, AB+
B+	B+, AB+
AB−	AB−, AB+
AB+	AB+ only
The implementation strictly uses recipient compatibility logic.

# 6. Web Dashboard Features

Built using Streamlit.
Features:
Mobile-friendly vitals input
Real-time physiological validation warnings
Risk prediction with confidence score 
Feature importance visualization
Strict compatible donor filtering
Emergency dispatch logic
Clean and minimal UI for healthcare workers

# 7. Tech Stack

Python
Scikit-learn
Pandas
Matplotlib
Joblib
Streamlit

# 8. Project Structure
Maternal-Guard/
│
├── app.py
├── maternal_risk_model.pkl
├── maternal_risk.csv
├── README.md
└── requirements.txt

# 9. How to Run

Install Dependencies:
pip install streamlit pandas scikit-learn matplotlib joblib
Run the Application:
python -m streamlit run app.py
Open in browser:
  http://localhost:8501

# 10. Security and Ethical Considerations

No patient data stored
Donor filtering strictly based on medical eligibility
No demographic bias features included
High-risk threshold tuned to reduce unnecessary panic triggers
Transparent model explainability through feature importance

# 11. Judging Alignment

This project satisfies the following rubric areas:
ML Accuracy (High Risk handling)
Reliability (Correct SOS trigger and donor return)
Scalability (Expandable donor database design)
Design (Usability for stressed healthcare workers)
As outlined in the official problem statement. 
Maternal-link problem statement…

# 12. Future Enhancements

Firebase or SQL-based donor database integration
Geolocation-based donor filtering
SMS or emergency notification integration
Admin dashboard for donor privacy management
Bias auditing and fairness evaluation

# Conclusion

Maternal-Guard & Life-Link integrates predictive Machine Learning, explainable AI, and medically accurate donor compatibility logic into a unified emergency response system.

The system demonstrates how AI can proactively identify maternal risk and reduce critical response time through structured digital intervention.
