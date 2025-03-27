import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Başlık ve açıklama
st.title("✍️ El Yazısı Rakam Tanıma")
st.subheader("Bir rakam görseli yükleyin, yapay zeka tahmin etsin!")

# Modeli yükle
model = load_model("mnist_model.h5")

# Görsel yükleme
uploaded_file = st.file_uploader("Bir görsel seçin (PNG, JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Görseli yükle ve işleme hazır hale getir
    image = Image.open(uploaded_file).convert("L")  # Gri ton
    image = ImageOps.invert(image)  # Siyah arka plan, beyaz rakam gibi işler
    image = image.resize((28, 28))  # MNIST boyutuna getir
    img_array = np.array(image) / 255.0  # Normalize et
    img_array = img_array.reshape(1, 28, 28, 1)  # CNN'e uygun forma getir

    # Tahmin yap
    prediction = model.predict(img_array)
    predicted_label = np.argmax(prediction)

    # Görseli ve sonucu göster
    st.image(image, caption="Yüklenen Görsel", width=150)
    st.success(f"📌 Tahmin Edilen Rakam: **{predicted_label}**")
