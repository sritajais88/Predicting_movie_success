
import streamlit as st
import pandas as pd
import joblib
import sklearn
print(sklearn.__version__)

# Load trained model
model = joblib.load("models/best_movie_model.pkl")
st.title("Movie Success Prediction App")

st.write("Enter movie details to predict the result")

# ---------- INPUT FEATURES ----------

color = st.selectbox("Color", ["Color", "Black and White"])

num_critic_for_reviews = st.number_input("Number of critic reviews", min_value=0)

duration = st.number_input("Duration (minutes)", min_value=0)

director_facebook_likes = st.number_input("Director Facebook Likes", min_value=0)

actor_3_facebook_likes = st.number_input("Actor 3 Facebook Likes", min_value=0)

actor_1_facebook_likes = st.number_input("Actor 1 Facebook Likes", min_value=0)

gross = st.number_input("Gross Revenue", min_value=0)

genres = st.text_input("Genres (e.g., Action,Drama)")

num_voted_users = st.number_input("Number of voted users", min_value=0)

cast_total_facebook_likes = st.number_input("Cast total Facebook likes", min_value=0)

facenumber_in_poster = st.number_input("Number of faces in poster", min_value=0)

num_user_for_reviews = st.number_input("Number of user reviews", min_value=0)

language = st.text_input("Language")

country = st.text_input("Country")

content_rating = st.selectbox("Content Rating", ["PG", "PG-13", "R", "G", "Not Rated"])

budget = st.number_input("Budget", min_value=0)

title_year = st.number_input("Title Year", min_value=1900)

actor_2_facebook_likes = st.number_input("Actor 2 Facebook Likes", min_value=0)

aspect_ratio = st.number_input("Aspect Ratio", min_value=0.0)

movie_facebook_likes = st.number_input("Movie Facebook Likes", min_value=0)

# ---------- PREDICTION BUTTON ----------

if st.button("Predict Movie Success"):

    input_data = pd.DataFrame({
        "color":[color],
        "num_critic_for_reviews":[num_critic_for_reviews],
        "duration":[duration],
        "director_facebook_likes":[director_facebook_likes],
        "actor_3_facebook_likes":[actor_3_facebook_likes],
        "actor_1_facebook_likes":[actor_1_facebook_likes],
        "gross":[gross],
        "genres":[genres],
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

    st.subheader("Prediction Result")
    st.write(prediction[0])