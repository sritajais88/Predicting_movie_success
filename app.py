
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("🎬 Movie IMDb Score Predictor")

st.write("Enter movie details to predict the IMDb score")

# ---- User Inputs ---- #

color = st.selectbox("Color", ["Color", "Black and White"])

num_critic_for_reviews = st.number_input("Number of Critic Reviews", min_value=0)

duration = st.number_input("Movie Duration (minutes)", min_value=1)

director_facebook_likes = st.number_input("Director Facebook Likes", min_value=0)

actor_1_facebook_likes = st.number_input("Actor 1 Facebook Likes", min_value=0)

actor_2_facebook_likes = st.number_input("Actor 2 Facebook Likes", min_value=0)

actor_3_facebook_likes = st.number_input("Actor 3 Facebook Likes", min_value=0)

gross = st.number_input("Gross Revenue", min_value=0)

num_voted_users = st.number_input("Number of Voted Users", min_value=0)

cast_total_facebook_likes = st.number_input("Total Cast Facebook Likes", min_value=0)

facenumber_in_poster = st.number_input("Number of Faces in Poster", min_value=0)

num_user_for_reviews = st.number_input("Number of User Reviews", min_value=0)

language = st.text_input("Language")

country = st.text_input("Country")

content_rating = st.text_input("Content Rating (PG, R, etc.)")

budget = st.number_input("Budget", min_value=0)

title_year = st.number_input("Release Year", min_value=1900, max_value=2030)

aspect_ratio = st.number_input("Aspect Ratio")

movie_facebook_likes = st.number_input("Movie Facebook Likes", min_value=0)

# ---- Prediction ---- #

if st.button("Predict IMDb Score"):

    input_data = pd.DataFrame({
        "color":[color],
        "num_critic_for_reviews":[num_critic_for_reviews],
        "duration":[duration],
        "director_facebook_likes":[director_facebook_likes],
        "actor_3_facebook_likes":[actor_3_facebook_likes],
        "actor_1_facebook_likes":[actor_1_facebook_likes],
        "gross":[gross],
        "num_voted_users":[num_voted_users],
        "cast_total_facebook_likes":[cast_total_facebook_likes],
        "facenumber_in_poster":[facenumber_in_poster],
        "num_user_for_reviews":[num_user_for_reviews],
        "language":[language],
        "country":[country],
        "content_rating":[content_rating],
        "budget":[budget],
        "title_year":[title_year],
        "actor_2_facebook_likes":[actor_2_facebook_likes],
        "aspect_ratio":[aspect_ratio],
        "movie_facebook_likes":[movie_facebook_likes]
    })

    prediction = model.predict(input_data)

    st.success(f"⭐ Predicted IMDb Score: {prediction[0]:.2f}")