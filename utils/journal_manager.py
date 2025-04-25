import os
from datetime import datetime

JOURNAL_DIR = "journal"

def write_private_entry(username, mood, journal_text, password):
    if not os.path.exists(JOURNAL_DIR):
        os.makedirs(JOURNAL_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(JOURNAL_DIR, f"journal_entry_{timestamp}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"[User] {username}\n")
        f.write(f"[Mood] {mood}\n")
        f.write(f"[Date] {timestamp}\n")
        f.write(f"[Password] {password}\n")
        f.write("\n[Entry]\n")
        f.write(journal_text)

    return filename
