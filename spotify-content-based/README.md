# 🎧 Spotify-Based Music Recommender

This is a simple content-based music recommendation system built using **Streamlit**, **pandas**, and **scikit-learn**.

It analyzes the musical features of songs (like danceability, energy, valence, and tempo) to suggest similar tracks.

---

## 🚀 Features

- Select a track from the list
- Instantly get 5 similar songs based on audio features
- Interactive user interface built with Streamlit

---

## 🧠 How It Works

1. Loads a sampled subset of the [Spotify 1921–2020 dataset](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks)
2. Normalizes key musical features
3. Calculates cosine similarity between tracks
4. Recommends the most similar ones to the selected song

---

## 🖼️ Screenshots

| Select Song | Get Recommendations |
|-------------|---------------------|
| ![song selection](images/song_selection_screen.png) | ![recommendations](images/music_recommendation_screen.png) |

---

## 📁 Project Structure

