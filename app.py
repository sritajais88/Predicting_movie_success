
import streamlit as st
import joblib
import pandas as pd

# load model
model = joblib.load("models/best_movie_model.pkl")

st.title("Movie Success Prediction")

budget = st.number_input("Budget")
votes = st.number_input("Number of Votes")

if st.button("Predict"):

    input_data = pd.DataFrame({
        "budget":[budget],
        "num_voted_users":[votes]
    })

    prediction = model.predict(input_data)

    st.write("Prediction:", prediction[0])