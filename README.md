# 🤖 Emoji Mood Prediction App – Backend

Welcome to the backend of the **Emoji Mood Prediction App** – a powerful AI-driven system that detects your mood using emoji reactions, speech, and facial expressions, then sends personalized insights directly to your email.

## 🚀 Key Features

- 🎭 **AI-Powered Mood Detection**
  - Speech-to-text analysis
  - Face recognition from webcam or image
  - Emoji-based emotion classification

- 🧠 **ML-based Mood Prediction**
  - No deep learning required
  - Lightweight, offline-compatible

- 📧 **Email Integration**
  - Automatic mood report sent to user email

- 🔐 **Login & Face Recognition Access**
  - Secure login
  - Offline face matching support

- 🕹️ **Offline & Online Support**
  - Runs without the internet
  - Local storage with cloud sync support

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Libraries:**  
  - `face_recognition`, `opencv-python`, `speechrecognition`, `nltk`, `smtplib`, `sklearn`, `numpy`, `pandas`
- **ML Model:** Trained model for mood classification (pre-trained `.pkl` file)
- **Storage:** Local JSON/CSV files (No database required)
- **Email:** SMTP (Gmail/Yahoo/Outlook supported)
