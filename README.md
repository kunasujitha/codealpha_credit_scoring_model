# codealpha_credit_scoring_model
Machine Learning based Credit Scoring Model that predicts customer credit risk using Logistic Regression and Random Forest Classifier with feature engineering, imbalance handling, ROC-AUC evaluation, and performance comparison.
# Credit Scoring Model using Machine Learning

## Project Overview

This project focuses on predicting customer credit risk using Machine Learning techniques. The model analyzes customer financial and behavioral features to classify customers into risk categories for credit assessment and loan approval decision-making.

The project includes:
- Data preprocessing
- Feature engineering
- Imbalanced data handling
- Logistic Regression
- Random Forest Classifier
- ROC-AUC evaluation
- Feature importance analysis

---

## Problem Statement

Financial institutions need reliable systems to identify risky customers before approving loans or credit cards. Incorrect credit risk prediction can lead to financial losses and loan defaults.

This project aims to build a machine learning-based credit scoring system that can effectively identify high-risk customers.

---

## Dataset Information

Dataset Source:
https://www.kaggle.com/datasets/programmer3/credit-worthiness-assessment-dataset

The dataset contains customer financial information such as:
- Income
- Debt ratios
- Payment history
- Number of loans
- Credit utilization
- Savings behavior
- Credit risk level

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Machine Learning Workflow

### 1. Data Preprocessing
- Checked missing values
- Handled duplicates
- Outlier analysis
- Feature scaling
- Train-test split using stratification

### 2. Feature Engineering
Created new financial indicators such as:
- Financial_Burden_Score
- Savings_Strength
- Credit_Discipline_Score

### 3. Handling Imbalanced Data
- Used class balancing techniques
- Applied stratified train-test split

### 4. Model Building
Implemented:
- Logistic Regression
- Random Forest Classifier

### 5. Model Evaluation
Evaluated models using:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC Score
- Confusion Matrix
- ROC Curve

---

## Results

### Logistic Regression
- Achieved strong classification performance
- Good recall for risky customers
- High ROC-AUC score

### Random Forest Classifier
- Improved nonlinear pattern learning
- Strong feature importance analysis
- Better overall classification performance

---

## ROC-AUC Analysis

ROC-AUC was used to evaluate the model’s ability to distinguish between risky and safe customers.

A strong ROC curve bending toward the top-left corner indicated:
- High True Positive Rate
- Low False Positive Rate

This demonstrated effective credit risk prediction capability.

---

## Feature Importance

Random Forest feature importance analysis identified the most influential features affecting customer credit risk prediction.

---

## Installation

Clone the repository:

```bash
git clone <your-github-repository-link>
```

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## How to Run the Project

Run the Jupyter Notebook or Python file:

```bash
jupyter notebook
```

OR

```bash
python credit_scoring_model.py
```

---

## Future Improvements

- Hyperparameter tuning
- XGBoost implementation
- Advanced imbalance handling techniques
- Model deployment using Flask or Streamlit
- Real-time credit scoring API

---

## Conclusion

This project successfully developed a machine learning-based credit scoring system capable of identifying risky customers effectively. The models demonstrated strong classification performance and can support financial institutions in credit risk assessment and loan approval decisions.

---

## Author

Sujitha Kuna

GitHub:
https://github.com/kunasujitha
