# 💳 Credit Risk Prediction System

## 📌 Project Overview

Credit risk assessment is a critical process in banking and financial institutions. Approving loans for high-risk customers can lead to financial losses, while rejecting creditworthy customers may reduce business opportunities.

This project uses Machine Learning techniques to predict whether a customer belongs to a **High Credit Risk** or **Low/Moderate Credit Risk** category based on their financial behavior, debt burden, income, payment history, and credit utilization patterns.

The project includes:

* Data Cleaning and Exploration
* Feature Engineering
* Handling Class Imbalance using SMOTE
* Logistic Regression Model
* Random Forest Classifier Model
* Model Evaluation using multiple metrics
* Credit Risk Prediction Web Application using Streamlit

---

## 🎯 Problem Statement

The goal of this project is to build a machine learning model that predicts a customer's credit risk level using financial history, income, debt behavior, and payment patterns.

This helps financial institutions:

* Reduce loan default risk
* Improve credit approval decisions
* Identify high-risk applicants early
* Support automated credit scoring systems

---

## 📊 Dataset

Dataset Source:

https://www.kaggle.com/datasets/programmer3/credit-worthiness-assessment-dataset

### Target Variable

| Target | Meaning                    |
| ------ | -------------------------- |
| 0      | Low / Moderate Credit Risk |
| 1      | High Credit Risk           |

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Imbalanced-Learn (SMOTE)
* Joblib
* Streamlit

---

## 📂 Project Structure

```
credit_scoring_model/
│
├── app.py
├── credit_scoring.py
├── credit_scoring_model.pkl
├── Pension_Credit_Assessment.csv
├── requirements.txt
├── README.md
│
├── visualizations/
│   ├── target_distribution.png
│   ├── correlation_heatmap.png
│   ├── logistic_regression_roc_curve.png
│   └── random_forest_roc_curve.png

```

---

## 🔍 Data Preprocessing

The following preprocessing steps were performed:

### Data Cleaning

* Checked missing values
* Checked duplicate records
* Verified data types
* Generated descriptive statistics

### Target Encoding

Original Classes:

```text
1 → Safe
2 → Moderate Risk
3 → High Risk
```

Converted into binary classification:

```text
1 → 0
2 → 0
3 → 1
```

Where:

* 0 = Low / Moderate Risk
* 1 = High Risk

### Outlier Treatment

Outliers in Monthly Income were removed using the IQR method.

### Handling Class Imbalance

SMOTE (Synthetic Minority Oversampling Technique) was applied only to the training dataset to balance the classes.

---

## ⚙️ Feature Engineering

Three additional financial indicators were created:

### Financial Burden Score

Combines:

* Debt-to-Income Ratio
* EMI-to-Income Ratio
* Missed Payments
* Number of Loans

Higher score indicates greater financial burden.

### Savings Strength

Combines:

* Savings-to-Income Ratio
* Emergency Fund Months

Higher score indicates stronger financial stability.

### Credit Discipline Score

Combines:

* Contribution Regularity
* Transaction Consistency Index

Measures responsible financial behavior.

---

## 📈 Selected Features

The final model was trained using:

* Debt_to_Income_Ratio
* Withdrawal_Frequency
* Missed_Payments_Last_12M
* Credit_Utilization_Rate
* financial_burden_score
* EMI_to_Income_Ratio
* Monthly_Income

---

## 🤖 Machine Learning Models

### 1. Logistic Regression

Pipeline:

* StandardScaler
* Logistic Regression

### Results

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 0.885 |
| Precision | 0.960 |
| Recall    | 0.899 |
| F1 Score  | 0.928 |
| ROC-AUC   | 0.946 |

---

### 2. Random Forest Classifier

Parameters:

* n_estimators = 100
* class_weight = balanced
* random_state = 42

### Results

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 0.895 |
| Precision | 0.949 |
| Recall    | 0.922 |
| F1 Score  | 0.935 |
| ROC-AUC   | 0.938 |

---

## 🏆 Final Model Selection

The Random Forest Classifier was selected as the final model because it achieved:

* Higher Recall
* Higher F1 Score
* Better overall performance on risky customer identification

In credit scoring, identifying risky customers is more important than maximizing accuracy alone.

---

## 📉 Model Evaluation

Evaluation metrics used:

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Classification Report
* Confusion Matrix
* ROC-AUC Score
* ROC Curve

---

## 🌐 Streamlit Web Application

A Streamlit application was developed to allow users to interact with the trained model.

### Features

* User-friendly interface
* Slider-based financial inputs
* Real-time credit risk prediction
* Prediction probability display
* Customer financial summary

### Run the Application

Install dependencies:

```
pip install -r requirements.txt
```

Start Streamlit:

```
streamlit run app.py
```


---

## 📚 Key Learnings

* Data preprocessing techniques
* Feature engineering for financial datasets
* Handling imbalanced data using SMOTE
* Logistic Regression and Random Forest modeling
* Model evaluation using ROC-AUC and Recall
* Building and deploying Streamlit applications

---

## 👨‍💻 Author

Kuna Sujitha

Aspiring Data Scientist | Machine Learning Enthusiast

GitHub: https://github.com/kunasujitha

LinkedIn: https://www.linkedin.com/in/kuna-sujitha-5014934b/
