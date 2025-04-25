def suggest_recipes(mood):
    recipes = {
        "happy": ["Fruit Salad 🍓", "Pasta Primavera 🍝"],
        "sad": ["Chocolate Cake 🍫", "Comfort Mac & Cheese 🧀"],
        "angry": ["Chilled Smoothie 🥤", "Cucumber Sandwich 🥪"],
        "neutral": ["Balanced Bowl 🥗", "Homestyle Roti 🌾"],
        "excited": ["Spicy Tacos 🌮", "Rainbow Veggie Wrap 🌯"],
        "calm": ["Herbal Tea 🍵", "Oats & Banana Bowl 🍌"],
        "stressed": ["Green Juice 🥬", "Dark Chocolate Almonds 🍫"]
    }

    return recipes.get(mood.lower(), ["Simple Salad 🥗", "Warm Soup 🍲"])
