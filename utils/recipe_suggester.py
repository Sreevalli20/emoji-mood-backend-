import json
import random
import os

DATA_FILE = os.path.join("data", "recipes.json")

def load_recipes():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"[Error] Failed to load recipes: {e}")
        return {}

def suggest_recipes(mood):
    mood = mood.lower()
    all_recipes = load_recipes()

    if mood in all_recipes:
        return random.sample(all_recipes[mood], min(2, len(all_recipes[mood])))
    else:
        return random.sample(all_recipes.get("neutral", []), 2)
