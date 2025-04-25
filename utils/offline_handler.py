from cryptography.fernet import Fernet
from datetime import datetime
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def save_result_offline(user_name, mood, quote, recipes, places):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = f"""----- Mood Entry ({timestamp}) -----
Name: {user_name}
Mood: {mood}
Quote: {quote}
Recipes: {', '.join(recipes)}
Places: {', '.join(places)}\n
"""

    if not os.path.exists("secret.key"):
        generate_key()
    key = load_key()
    fernet = Fernet(key)

    encrypted_data = fernet.encrypt(result.encode())

    with open("offline_results.txt", "ab") as file:
        file.write(encrypted_data + b"\n")

    print("[🔐] Offline mood result saved and encrypted.")
