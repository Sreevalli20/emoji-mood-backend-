import os
import datetime
from utils.face_analyzer import analyze_face_mood
from utils.voice_analyzer import analyze_voice_mood
from utils.quote_generator import get_quote
from utils.recipe_suggester import suggest_recipes
from utils.place_suggester import suggest_places
from utils.database import save_mood_data
from utils.mood_trend_analyzer import analyze_mood_trends
from utils.journal_writer import write_private_entry
from utils.ai_suggestions import get_ai_suggestions
from utils.offline_handler import save_result_offline

def print_line():
    print("-" * 50)

def run_app():
    print("🧠 Welcome to Emoji Mood Prediction App!\n")

    user_name = input("👤 Enter your Name: ")
    email = input("📧 Enter your Zoho Email (sender & receiver): ")
    app_password = input("🔑 Enter your Zoho App Password: ")

    print("\n📸 Capturing facial emotion...")
    face_mood, face_score, face_emotions = analyze_face_mood()
    print(f"[✅] Face Mood: {face_mood} | Score: {face_score}")

    print("\n🎙️ Recording voice and analyzing tone...")
    voice_mood, voice_score, voice_report = analyze_voice_mood()
    print(f"[✅] Voice Mood: {voice_mood} | Score: {voice_score}")

    feeling = input("\n⌨️ Please describe your current feeling:\n💬 You: ").lower()

    # Mood voting logic
    mood_votes = [face_mood, voice_mood]
    if "sad" in feeling or "bad" in feeling:
        mood_votes.append("sad")
    elif "happy" in feeling or "good" in feeling:
        mood_votes.append("happy")
    elif "angry" in feeling:
        mood_votes.append("angry")
    else:
        mood_votes.append("neutral")

    final_mood = max(set(mood_votes), key=mood_votes.count)

    print_line()
    print(f"🧠 Final Predicted Mood: {final_mood.upper()}")
    print_line()

    # Suggestions & Results
    quote = get_quote(final_mood)
    recipes = suggest_recipes(final_mood)
    places = suggest_places(final_mood)
    suggestions = get_ai_suggestions(final_mood)

    print(f"\n💡 Motivational Quote: {quote}")
    print(f"\n🥗 Recipes: {', '.join(recipes)}")
    print(f"\n📍 Places to Visit: {', '.join(places)}")
    print(f"\n🎯 AI Suggestions: {', '.join(suggestions)}")

    # Save mood data
    try:
        save_mood_data(user_name, final_mood, quote, recipes, places)
    except Exception as e:
        print(f"[Error] Saving mood data failed: {e}")
        save_result_offline(user_name, final_mood, quote, recipes, places)

    # Email sending
    try:
        from utils.mailer import send_mood_email
        send_mood_email(email, app_password, user_name, final_mood, quote, recipes, places, suggestions)
    except Exception as e:
        print(f"[Warning] Email sending failed: {e}")
        save_result_offline(user_name, final_mood, quote, recipes, places)

    # Weekly Mood Trend
    print("\n📊 Weekly Mood Trend Analysis:")
    trend = analyze_mood_trends()
    if trend:
        for mood, count in trend.items():
            print(f"  • {mood.capitalize()} - {count} times")
    else:
        print("  [ℹ️] No trend data available.")

if __name__ == "__main__":
    name = input("👤 Enter your name: ")
    mood = input("😊 What's your current mood (happy/sad/angry/etc.): ")
    write_journal = input("📝 Do you want to write a private journal entry? (yes/no): ").lower()

    if write_journal == "yes":
        journal_text = input("Enter your thoughts: ")
        password = input("Set a password to protect this entry: ")
        journal_file = write_private_entry(name, mood, journal_text, password)
        print(f"✅ Journal entry saved to {journal_file}")

    run_app()
