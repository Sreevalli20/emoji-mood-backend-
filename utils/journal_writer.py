# utils/journal_writer.py

import os
from datetime import datetime

def write_private_entry(name, mood, thoughts, password):
    # Ensure journal directory exists
    journal_dir = os.path.join("journal")
    os.makedirs(journal_dir, exist_ok=True)

    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{name}_{timestamp}.txt"
    filepath = os.path.join(journal_dir, filename)

    # Save content with password protection notice
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("🔒 This entry is password-protected.\n")
        f.write(f"Password: {password}\n")
        f.write(f"Name: {name}\nMood: {mood}\n")
        f.write("Thoughts:\n")
        f.write(thoughts + "\n")

    print(f"✅ Journal entry saved to {filepath}")
    return filepath
