# utils/face_analyzer.py

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Disable oneDNN for faster startup

from deepface import DeepFace
import cv2

def analyze_face_mood():
    print("🔍 Scanning your face... Please look at the camera.")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[Error] Unable to access the camera.")
        return "neutral", 5, {}

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("[Error] Failed to capture image.")
        return "neutral", 5, {}

    try:
        # Lightweight emotion analysis using opencv backend
        result = DeepFace.analyze(
            img_path=frame,
            actions=['emotion'],
            enforce_detection=False,
            detector_backend='opencv'  # ⚡ Faster and avoids TensorFlow
        )[0]

        dominant_emotion = result['dominant_emotion']
        emotion_scores = result['emotion']

        print("\n📊 Facial Emotion Scores:")
        for emo, val in emotion_scores.items():
            print(f"  • {emo.capitalize():<10}: {round(val, 2)}")

        score = int(emotion_scores[dominant_emotion] / 10)
        return dominant_emotion, score, emotion_scores

    except Exception as e:
        print(f"[Error] DeepFace Analysis Failed: {e}")
        return "neutral", 5, {}
