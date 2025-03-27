# Turkish Tweet Sentiment Analysis

This project performs sentiment classification on Turkish tweets into 5 emotion categories:

- Anger (`kızgın`)
- Happy (`mutlu`)
- Sad (`üzgün`)
- Surprise (`surpriz`)
- Fear (`korku`)

---

## 🔧 Methods Used

- Text vectorization using **TF-IDF**
- Classification with **Logistic Regression**
- Label encoding of sentiment classes

---

## 📈 Model Performance

- ✅ **97% accuracy** on test set
- ⚖️ F1-scores range from **0.96 to 0.98**
- 🧠 Balanced results across all emotion labels

---

## 🧪 Summary

The model can accurately classify Turkish tweets into emotional categories such as  
*anger, happiness, sadness, surprise*, and *fear*.  
It is trained on a balanced dataset with strong generalization ability.

---

## 📁 Dataset

- Source: [Kaggle - anil1055/turkish-tweet-dataset](https://www.kaggle.com/datasets/anil1055/turkish-tweet-dataset)
- File used: `data/turkish_tweets.xlsx`

---

## 📍 Notes

- The main notebook is written in **Turkish**
- Predictions can be made with custom tweet input in real-time
