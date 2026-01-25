# 🎵 Mood-Based Music Recommendation System

[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-ready-brightgreen)](https://streamlit.io/)

A **mood-driven music recommendation system** that suggests songs based on your current emotional state. Select your mood, and the system provides a curated list of songs that fit your vibe.

---

## Features

- Predicts song mood using a pre-trained machine learning model.
- Interactive interface to select your current mood.
- Provides up to 10 randomized song recommendations matching the chosen mood.
- Lightweight and easy to run locally.

---

## Project Structure

├── mood_music_system.ipynb # Notebook for model development and analysis
├── app.py # Streamlit application
├── labeled_music_data.csv # Dataset with song details and predicted moods
├── music_data.csv # Original music dataset
└── song_mood_model.pkl # Pre-trained mood prediction model

yaml
Copy code

---

## Getting Started

### Prerequisites

- Python 3.9+
- Install required packages:

```bash
pip install pandas streamlit joblib
