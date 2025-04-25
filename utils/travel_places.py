def suggest_places(mood):
    places = {
        "happy": ["Park Walk 🌳", "Coffee Shop ☕"],
        "sad": ["Quiet Library 📚", "Nature Trail 🍃"],
        "angry": ["Open Field 🏞️", "Jogging Track 🏃"],
        "neutral": ["Museum 🖼️", "City Stroll 🚶‍♂️"],
        "excited": ["Amusement Park 🎢", "Art Class 🎨"],
        "calm": ["Meditation Center 🧘", "Bookstore 📖"],
        "stressed": ["Spa 💆", "Botanical Garden 🌸"]
    }

    return places.get(mood.lower(), ["Home Garden 🌼", "Balcony View 🌇"])
