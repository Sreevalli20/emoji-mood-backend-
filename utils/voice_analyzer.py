# utils/voice_analyzer.py

import speech_recognition as sr
from textblob import TextBlob
import re

def analyze_voice_mood():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[🎙️ Voice] Listening for 5 seconds...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            text = r.recognize_google(audio)
            print(f"\n🗣️ Transcribed: \"{text}\"")

            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            # Sentiment Label
            if polarity > 0.4:
                mood = "happy"
            elif polarity < -0.4:
                mood = "sad"
            elif -0.4 <= polarity <= 0.4 and subjectivity > 0.5:
                mood = "angry"
            else:
                mood = "neutral"

            print("\n📊 Voice Sentiment Breakdown:")
            print(f"  • Sentiment Polarity: {round(polarity, 2)}")
            print(f"  • Subjectivity Level: {round(subjectivity, 2)}")
            print(f"  • Voice Mood Predicted: {mood.upper()}")

            score = int(abs(polarity) * 10) + 5
            return mood, score, {
                "text": text,
                "polarity": polarity,
                "subjectivity": subjectivity
            }

        except sr.WaitTimeoutError:
            print("[Error] Timeout: No voice detected.")
            return "neutral", 5, {}
        except sr.UnknownValueError:
            print("[Error] Couldn't understand audio.")
            return "neutral", 5, {}
        except sr.RequestError as e:
            print(f"[Error] API Error: {e}")
            return "neutral", 5, {}
