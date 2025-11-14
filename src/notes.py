import json
import os

NOTES_FILE = "data/notes.json"

def save_note(question, answer):
    note = {"question": question, "answer": answer}
    data = []

    if os.path.exists(NOTES_FILE):
        data = json.load(open(NOTES_FILE, "r"))

    data.append(note)
    json.dump(data, open(NOTES_FILE, "w"), indent=2)

def load_notes():
    if os.path.exists(NOTES_FILE):
        return json.load(open(NOTES_FILE, "r"))
    return []
