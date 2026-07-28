from contextlib import redirect_stdout
import json
import os
import time

# --- 1. FILE HANDLING FUNCTIONS ---
DATA_FILE = "students_data.json"


def load_students():
    """Loads student data from a file on startup."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}  # Return empty dictionary if file doesn't exist yet