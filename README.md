# mood music

pick a mood. get songs that match it.

a lightweight ML model runs behind the scenes, classifying songs by emotional tone and serving up to 10 recommendations based on whatever you're feeling. no account needed, no data collected, runs entirely on your machine.

---

## run it

```bash
pip install pandas streamlit joblib
streamlit run app.py
```

---

## files

```
mood_music_system.ipynb   # model training
app.py                    # the app
labeled_music_data.csv    # labeled dataset
music_data.csv            # raw song data
song_mood_model.pkl       # trained model
```

---

## stack

Python 3.9+, Streamlit, scikit-learn, pandas
