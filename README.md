# ANN_Regression_SalaryPrediction
## Overview
This project predicts the estimated salary of individuals based on various input features such as geography, gender, age, credit score, and account-related information. It uses a neural network regression model implemented in TensorFlow and integrated with a Streamlit web application for easy interaction.

## Features
User Input: Input fields for user details like geography, gender, age, and financial metrics.
Data Preprocessing:
Categorical features like geography and gender are encoded using OneHotEncoder and LabelEncoder.
Numeric features are scaled using StandardScaler.
Prediction: A trained regression model predicts the estimated salary based on processed inputs.
Interactive Web App: Built with Streamlit for a user-friendly interface.

## Installation
Prerequisites
Ensure the following are installed on your system:

Python 3.8+
TensorFlow
Streamlit
Pandas
Scikit-learn
Pickle (for saving/loading encoders and scalers)
