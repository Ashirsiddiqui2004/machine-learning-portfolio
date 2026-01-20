# RNN Sentiment Analysis (IMDB Reviews)

This project implements a **Recurrent Neural Network (RNN)** from scratch
to perform **sentiment analysis** on movie reviews.

The goal is to understand how RNNs process **sequential text data**
and why they struggle with long-term dependencies.

---

## 📌 Dataset
- **IMDB Movie Reviews**
- Loaded using `tensorflow_datasets`
- Binary labels:
  - `0` → Negative
  - `1` → Positive

---

## 🧠 Model Architecture

- TextVectorization (text → integers)
- Embedding Layer
- SimpleRNN Layer
- Dense Output Layer (Sigmoid)

---

## 🔍 Key Concepts Covered

- Sequential data processing
- Word embeddings
- Recurrent neural networks (RNN)
- Vanishing gradient problem
- Binary text classification

---

## ⚠️ Limitations

- Simple RNN struggles with long-term dependencies
- Performance is limited on long reviews

This motivates the use of **LSTM**, which is covered in the next project.

---

## 🚀 Tech Stack

- Python
- TensorFlow / Keras
- TensorFlow Datasets
- Matplotlib

---

## 📈 Result

The model successfully learns sentiment patterns but shows
limitations on long sequences, demonstrating why RNNs
are often replaced by LSTM in practice.
