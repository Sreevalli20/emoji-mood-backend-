import random

places_by_mood = {
    "happy": [
        "🎡 Amusement Park",
        "🏞️ Nature Trail",
        "🏖️ Beach with Friends"
    ],
    "sad": [
        "🧘 Meditation Center",
        "📚 Library for Peaceful Reading",
        "🌄 Solo Mountain Viewpoint"
    ],
    "angry": [
        "🥊 Kickboxing Class",
        "🏋️‍♀️ Gym for Workout",
        "🏞️ Silent Walk in Nature"
    ],
    "neutral": [
        "☕ Quiet Café",
        "🎬 Movie Theatre",
        "🖼️ Art Museum"
    ],
    "stressed": [
        "💆 Spa or Massage Centre",
        "🌸 Botanical Garden",
        "🚶‍♂️ Light Walk in Park"
    ],
    "excited": [
        "🎉 Live Music Concert",
        "🎢 Adventure Park",
        "🎮 Gaming Arena"
    ]
}

def suggest_places(mood):
    mood = mood.lower()
    return random.sample(places_by_mood.get(mood, places_by_mood["neutral"]), 2)
