import json
import csv
import os
from datetime import datetime

JSON_FILE = os.path.join("data", "mood_history.json")
CSV_FILE = os.path.join("data", "mood_history.csv")

def save_mood_data(name, mood, quote, recipes, places):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mood_entry = {
        "name": name,
        "mood": mood,
        "quote": quote,
        "recipes": recipes,
        "places": places,
        "timestamp": timestamp
    }

    # Save to JSON
    try:
        data = []
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        data.append(mood_entry)
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("[✅] Mood data saved to JSON.")
    except Exception as e:
        print(f"[❌] Error saving to JSON: {e}")

    # Save to CSV
    try:
        write_header = not os.path.exists(CSV_FILE)
        with open(CSV_FILE, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(["Name", "Mood", "Quote", "Recipes", "Places", "Timestamp"])
            writer.writerow([
                name,
                mood,
                quote,
                "; ".join(recipes),
                "; ".join(places),
                timestamp
            ])
        print("[✅] Mood data saved to CSV.")
    except Exception as e:
        print(f"[❌] Error saving to CSV: {e}")
