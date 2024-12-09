import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Load the trained data
model = tf.keras.models.load_model('regression_model.h5')



# Load the encoder and scaler
with open('one_hot_geo.pkl', 'rb') as file:
    label_encoder_geo=pickle.load(file)

with open('label_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scal.pkl','rb') as file:
    scaler = pickle.load(file)


# Streamlit app
st.title('Estimated Salary Prediction')

# User Input

geography = st.selectbox('Geography',  label_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 100)
balance = st.number_input('Balance')
cretit_score = st.number_input('Credit Score')
exited = st.selectbox('Exited', [0,1])
tenure = st.slider('Tenture', 0 , 10)
num_of_products = st.slider('Number of products', 1,4)
has_cr_card = st.selectbox("Has Credit Card", [0,1])
is_active_member = st.selectbox('Is Active Member', [0,1])


# Prepare the Input Data

input_data = pd.DataFrame({
    'CreditScore' : [cretit_score],
    'Gender' : [label_encoder_gender.transform([gender])[0]],
    'Age' : [age],
    'Tenure' : [tenure],
    'Balance': [balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'Exited':[exited]
})

# One HOt encoder geography
geo_encode = label_encoder_geo.transform([[geography]]).toarray()
geo_encode_df = pd.DataFrame(geo_encode, columns=label_encoder_geo.get_feature_names_out(['Geography']))


# Combine one-hot-encoded coloums with input
input_data = pd.concat([input_data.reset_index(drop = True), geo_encode_df], axis = 1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)


# Predict Churn
prediction = model.predict(input_data_scaled)
prediction_pro = prediction[0][0]

st.write(f'Predicted estimated salary: {prediction_pro:.2f}')