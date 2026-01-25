import streamlit as st
import pandas as pd
import joblib
import random

model = joblib.load("song_mood_model.pkl")
df = pd.read_csv("labeled_music_data.csv")

st.title("🎵 Mood-Based Music Recommendation System")
st.markdown("Select your current mood to get song suggestions that match your vibe.")

mood_options = df['predicted_mood'].unique().tolist()
user_mood = st.selectbox("What's yor current mood?", options=sorted(mood_options))

if st.button("Recommend Songs"):
    filtered_songs = df[df['predicted_mood'] == user_mood]

    if not filtered_songs.empty:
        recommended = filtered_songs.sample(n=min(10, len(filtered_songs)), random_state=42)
        st.subheader(f"🎶 Recommended Songs for '{user_mood}' Mood")
        for idx, row in recommended.iterrows():
            st.markdown(f"**{row['name']}** by *{row['artist']}*  ")
    else:
        st.warning("No songs found for this mood.")