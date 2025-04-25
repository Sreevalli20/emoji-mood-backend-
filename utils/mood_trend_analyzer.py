# utils/mood_trend_analyzer.py

import json
from collections import Counter
from datetime import datetime, timedelta
import os

MOOD_HISTORY_FILE = os.path.join("data", "mood_history.json")

def analyze_mood_trends(days=7):
    try:
        if not os.path.exists(MOOD_HISTORY_FILE):
            print("[⚠️] No mood history found.")
            return {}

        with open(MOOD_HISTORY_FILE, "r", encoding="utf-8") as f:
            mood_data = json.load(f)

        cutoff_date = datetime.now() - timedelta(days=days)
        recent_entries = []

        for entry in mood_data:
            timestamp = entry.get("timestamp")
            if not timestamp:
                continue

            # Try parsing with microseconds first, fallback to seconds
            try:
                dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
            except ValueError:
                try:
                    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    continue  # Skip bad format

            if dt >= cutoff_date:
                recent_entries.append(entry)

        if not recent_entries:
            print(f"[ℹ️] No entries in the last {days} days.")
            return {}

        moods = [entry["mood"] for entry in recent_entries]
        mood_counts = Counter(moods)

        print(f"\n📊 Mood Trends in Last {days} Days:")
        for mood, count in mood_counts.items():
            emoji = {
                "happy": "🙂", "sad": "😞", "neutral": "😐", "angry": "😠",
                "excited": "😄", "calm": "😌", "stressed": "😰"
            }.get(mood.lower(), "")
            print(f"{emoji} {mood.capitalize()} - {count} times")

        most_common = mood_counts.most_common(1)[0][0]

        suggestion = {
            "sad": "Try journaling or calling a friend.",
            "stressed": "Try deep breathing for 5 mins.",
            "angry": "Listen to calming music or go for a walk.",
            "neutral": "Try doing something new today!",
            "happy": "Keep it up! Spread the joy!",
            "calm": "Keep up the peace! Maybe meditate more.",
            "excited": "Channel that energy into something creative!"
        }.get(most_common.lower(), "Stay positive!")

        print(f"\n➡ Suggested Activity: {suggestion}\n")

        return dict(mood_counts)

    except Exception as e:
        print(f"[❌] Error analyzing trends: {e}")
        return {}
