# main.py

import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Sayfa başlığı
st.title("🎵 Spotify Music Recommender")
st.write("Bir şarkı seç, sana benzerlerini önerelim 🎧")

# Veriyi yükle (örneklenmiş)
@st.cache_data
def load_data():
    df = pd.read_csv("data/tracks.csv", encoding="latin1", low_memory=False)
    df = df[['name', 'artists', 'danceability', 'energy', 'valence', 'tempo']]
    df.dropna(inplace=True)

    # 🔥 Bellek dostu örnekleme (5K)
    df_sampled = df.sample(n=15000, random_state=42).reset_index(drop=True)
    return df_sampled

df = load_data()

# Özellikleri normalize et
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['danceability', 'energy', 'valence', 'tempo']])

# Benzerlik matrisi oluştur (örnekle sınırlı!)
similarity_matrix = cosine_similarity(X_scaled)

# Kullanıcıdan şarkı seçimi
song_names = df['name'].tolist()
selected_song = st.selectbox("Bir şarkı seçin 🎧", song_names)

# Butona basıldığında önerileri göster
if st.button("🎯 Benzer şarkıları getir"):
    song_index = df[df['name'] == selected_song].index[0]
    similar_indices = similarity_matrix[song_index].argsort()[::-1][1:6]
    recommended = df.iloc[similar_indices][['name', 'artists']]

    st.subheader("🎶 Önerilen Şarkılar:")
    for i, row in recommended.iterrows():
        st.write(f"**{row['name']}** by *{row['artists']}*")
