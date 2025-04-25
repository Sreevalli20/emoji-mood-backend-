def get_quote(mood):
    quotes = {
        "happy": "Happiness is not by chance, but by choice.",
        "sad": "Every storm runs out of rain.",
        "angry": "For every minute you remain angry, you give up sixty seconds of peace.",
        "neutral": "Balance is the key to everything.",
        "excited": "Let your enthusiasm shine brighter than your fears.",
        "calm": "Peace comes from within. Do not seek it without.",
        "stressed": "You can do anything, but not everything. Take a breath."
    }

    return quotes.get(mood.lower(), "Keep going, better days are coming!")
