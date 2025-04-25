def get_ai_suggestions(mood):
    mood = mood.lower()

    suggestions = {
        "happy": {
            "meditation": "Keep the positivity! Try 5 mins of gratitude journaling.",
            "music": ["Happy Vibes Playlist 🎵", "Dance Beats 💃"],
            "todo": "Share your joy with others. Do something kind today."
        },
        "sad": {
            "meditation": "Try a 10-minute calming meditation on YouTube.",
            "music": ["Soothing Acoustic 🎸", "Uplifting Instrumentals 🎧"],
            "todo": "Write about how you feel. Talk to a friend."
        },
        "angry": {
            "meditation": "Do 4-7-8 breathing for 2 minutes.",
            "music": ["Peaceful Piano 🎹", "Nature Sounds 🌿"],
            "todo": "Take a walk or do light exercise to release anger."
        },
        "neutral": {
            "meditation": "Mindfulness check-in – how are you really feeling?",
            "music": ["Lo-fi Chill 🎼", "Focus Music 🎯"],
            "todo": "Set 1 goal for today and work on it mindfully."
        },
        "excited": {
            "meditation": "Quick energizing breath work to focus your energy.",
            "music": ["Electro Pop ⚡", "Workout Tunes 💪"],
            "todo": "Use this boost to start a creative project!"
        },
        "calm": {
            "meditation": "Reflect and enjoy your peace. Light yoga can help.",
            "music": ["Relaxing Ocean Sounds 🌊", "Instrumental Chill 🎻"],
            "todo": "Journal a gratitude list or read something meaningful."
        },
        "stressed": {
            "meditation": "Try body scan meditation for 5 minutes.",
            "music": ["Deep Relaxation 🎶", "Breath-focused Calm Tracks 🧘"],
            "todo": "List 3 things you can control right now."
        },
        "bored": {
            "meditation": "Stimulate your curiosity with a new podcast or book.",
            "music": ["Indie Mix 🎧", "Adventure Playlist 🌍"],
            "todo": "Try a new hobby or explore something creative."
        },
        "tired": {
            "meditation": "Do a quick 5-minute guided rest meditation.",
            "music": ["Soft Piano 🌙", "Sleepy Vibes 🎼"],
            "todo": "Power nap or stretch – recharge yourself gently."
        },
        "anxious": {
            "meditation": "Try grounding techniques – focus on your breath.",
            "music": ["Anxiety Relief Tracks 🎶", "Slow Lo-fi Chill 🎧"],
            "todo": "Write your thoughts down or practice 3-3-3 method."
        }
    }

    # Check for best matching base mood
    for base_mood in suggestions:
        if base_mood in mood:
            return suggestions[base_mood]

    # Default fallback
    return {
        "meditation": "Take a deep breath. You got this!",
        "music": ["Default Peace Track 🎶"],
        "todo": "Stay grounded. Write down your feelings."
    }

