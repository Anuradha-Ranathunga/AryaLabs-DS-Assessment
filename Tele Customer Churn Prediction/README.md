# Telecom-Customer-Churn-Prediction

## What is Churn?

Customer churn, also known as customer attrition, refers to the situation where customers discontinue their relationship with a business, stop using its products or services, or switch to a competitor. This is a critical metric for businesses, particularly those in industries where customer retention plays a vital role in long-term growth and profitability. Reducing churn is often more cost-effective than acquiring new customers, making it a key focus for many companies.

Understanding the factors that drive churn, such as poor service, high prices, or unmet expectations, is essential for businesses aiming to improve customer satisfaction. Strategies to reduce churn often involve offering personalized experiences, addressing customer concerns, and continually enhancing products or services. By predicting which customers are at risk of leaving, companies can take proactive steps to retain them, ultimately fostering a loyal customer base and sustaining growth.

## Dataset:

The Telecom Customer Churn Dataset is sourced from Kaggle and is used to predict customer churn in the telecom industry. It contains various customer attributes, including demographic information, account details, and services used, which help predict the likelihood of a customer leaving the telecom company. The goal is to analyze these attributes and identify patterns or behaviors that lead to churn, enabling businesses to take preventive measures.

### Key Features in the Dataset:
The dataset contains several features related to customers' demographics, services, and account information. The most important features are:

- CustomerID: A unique identifier for each customer.
- Gender: Gender of the customer (Male/Female).
- SeniorCitizen: Whether the customer is a senior citizen (1 = Yes, 0 = No).
- Tenure: The number of months the customer has been with the company.
- PhoneService: Whether the customer has phone service (Yes/No).
- InternetService: Type of internet service the customer uses (DSL/Fiber optic/No).
- Contract: The type of contract the customer has (Month-to-month, One year, Two year).
- PaperlessBilling: Whether the customer has opted for paperless billing (Yes/No).
- MonthlyCharges: The amount the customer is charged per month.
- Churn: Whether the customer has churned (1 = Churned, 0 = Stayed).

**Dataset URL:**
[Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

This dataset serves as the foundation for building predictive models that can identify customers likely to churn, allowing businesses to take actions to reduce churn rates and enhance customer retention strategies.

### Data Preprocessing:
1. The dataset contains both categorical and numerical features.
2. Missing values may need to be handled, especially for fields like TotalCharges where some customers have missing entries.
3. Some categorical features (e.g., InternetService, Contract) may require encoding (e.g., one-hot encoding) to be used in machine learning models.
4. Tenure and MonthlyCharges are continuous variables that may require scaling for some algorithms.

## Installation

To get started with this project, follow these steps to set it up on your local machine:

1. Clone the repository:
`git clone https://github.com/Anuradha-Ranathunga/Telecom-Customer-Churn-Prediction.git`

2. Navigate to the project directory:
`cd Telecom-Customer-Churn-Prediction`

3. Install the required dependencies:
`pip install -r requirements.txt`

## Usage

1. **Load the Dataset:** The dataset is in CSV format and can be loaded using Python libraries like Pandas.
```
import pandas as pd
data = pd.read_csv('telecom_data.csv')
```
2. **Data Preprocessing:**
- Handle missing values (if any).
- Encode categorical variables (e.g., Contract, Gender).
- Scale numerical features (e.g., MonthlyCharges, Tenure) for model training.

3. **Train/Test Split:** Split the data into training and testing sets to evaluate the model's performance.
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

4. **Model Training:** Train machine learning models such as Logistic Regression, Random Forest, and XGBoost.
```
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

5. **Model Evaluation:** Evaluate the model using accuracy, precision, recall, F1-score, and ROC-AUC to determine how well the model is performing.
```
from sklearn.metrics import classification_report, accuracy_score
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
```

## Model Evaluation

The model's performance is evaluated using the following classification metrics:

- **Accuracy:** The percentage of correct predictions.
- **Precision:** The proportion of true positive predictions among all positive predictions.
- **Recall:** The proportion of true positives correctly identified.
- **F1-Score:** The harmonic mean of precision and recall, providing a balance between the two.
- **ROC-AUC:** Measures the area under the ROC curve, which is useful for understanding how well the model distinguishes between the two classes (churn and no churn).
