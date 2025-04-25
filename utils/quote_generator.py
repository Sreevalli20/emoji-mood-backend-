import random

quotes = {
    "happy": [
        "Happiness is a direction, not a place.",
        "Stay positive, work hard, make it happen!",
        "Smiles are contagious – keep spreading them!"
    ],
    "sad": [
        "This too shall pass.",
        "Tough times never last, but tough people do.",
        "Crying doesn't mean you're weak—it means you've been strong for too long."
    ],
    "angry": [
        "Take a deep breath and count to ten.",
        "The best fighter is never angry.",
        "Anger doesn't solve anything—it builds nothing."
    ],
    "neutral": [
        "Keep going. Everything you need will come to you.",
        "Life is about balance. Breathe. Let go.",
        "Sometimes not doing anything is doing something important."
    ],
    "stressed": [
        "Relax. Recharge. Reconnect.",
        "Take things one step at a time.",
        "Stress is not what happens to us. It's our response to it."
    ],
    "excited": [
        "Your excitement is a sign you're doing something right!",
        "Stay pumped and spread the good energy!",
        "The best is yet to come!"
    ]
}

def get_quote(mood):
    mood = mood.lower()
    return random.choice(quotes.get(mood, quotes["neutral"]))
