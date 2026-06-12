import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("credit_scoring_model.pkl")

# Page Config
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="wide"
)

# Title
st.title("💳 Credit Risk Prediction System")
st.write(
    """
    Enter customer financial information below to predict
    whether the customer is a **High Risk** or **Low/Moderate Risk**
    credit applicant.
    """
)

# Create Two Columns
col1, col2 = st.columns(2)

with col1:

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

    debt_to_income_ratio = st.slider(
        "Debt To Income Ratio (%)",
        min_value=0.0,
        max_value=100.0,
        value=30.0,
        step=0.1,
        help="Percentage of income used to pay debts"
    )

    emi_to_income_ratio = st.slider(
        "EMI To Income Ratio (%)",
        min_value=0.0,
        max_value=100.0,
        value=20.0,
        step=0.1
    )

    credit_utilization_rate = st.slider(
        "Credit Utilization Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=0.1
    )

with col2:

    withdrawal_frequency = st.slider(
        "Withdrawal Frequency",
        min_value=0,
        max_value=50,
        value=5
    )

    missed_payments = st.slider(
        "Missed Payments Last 12 Months",
        min_value=0,
        max_value=20,
        value=0
    )

    number_of_loans = st.slider(
        "Number Of Loans",
        min_value=0,
        max_value=20,
        value=2
    )

# Prediction Button
if st.button("Predict Credit Risk"):

    # Feature Engineering
    financial_burden_score = (
        debt_to_income_ratio
        + emi_to_income_ratio
        + missed_payments
        + number_of_loans
    )

    # DataFrame
    input_data = pd.DataFrame({
        "Debt_to_Income_Ratio": [debt_to_income_ratio],
        "Withdrawal_Frequency": [withdrawal_frequency],
        "Missed_Payments_Last_12M": [missed_payments],
        "Credit_Utilization_Rate": [credit_utilization_rate],
        "financial_burden_score": [financial_burden_score],
        "EMI_to_Income_Ratio": [emi_to_income_ratio],
        "Monthly_Income": [monthly_income]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0]

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error(
            "⚠️ High Credit Risk Customer"
        )

        st.metric(
            "Risk Probability",
            f"{probability[1]*100:.2f}%"
        )

    else:

        st.success(
            "✅ Low / Moderate Credit Risk Customer"
        )

        st.metric(
            "Safety Probability",
            f"{probability[0]*100:.2f}%"
        )

    st.divider()

    st.subheader("Customer Summary")

    st.dataframe(input_data)

# Footer
st.markdown("---")
st.caption(
    "Built using Machine Learning (Random Forest Classifier) and Streamlit"
)