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

def save_students():
    """Saves the current global stds dictionary to the file."""
    with open(DATA_FILE, "w") as file:
        json.dump(stds, file, indent=4)
# --- 2. INITIALIZE DATA ---
# Load saved data
stds = load_students()

colour = "red"


def std_add(Name):
    global stds

    Grade = input("Class: ")
    roll_no = input("Roll no: ")
    Session = input("Session: ")

    stds[Name] = {"Class: ": Grade, "roll no: ": roll_no, "session: ": Session}

    English = 0
    Physics = 0
    Chemistry = 0
    Computer_Science = 0

    try:
        English = int(input("Enter Marks in English: "))
    except ValueError:
        print("INVALID INPUT")

    try:
        Physics = int(input("Enter Marks in Physics: "))
    except ValueError:
        print("INVALID INPUT")

    try:
        Chemistry = int(input("Enter Marks in Chemistry: "))
    except ValueError:
        print("INVALID INPUT")

    maths_in = input("Enter Marks in Maths(press enter for N/A): ")
    Maths = int(maths_in) if maths_in.strip() != "" else "N/A"

    bio_in = input("Enter Marks in Biology(press enter for N/A): ")
    Biology = int(bio_in) if bio_in.strip() != "" else "N/A"

    try:
        Computer_Science = int(input("Enter Marks in Computer Science: "))
    except ValueError:
        print("INVALID INPUT")

    Marks = {
        "English: ": English,
        "Physics: ": Physics,
        "Chemistry: ": Chemistry,
        "Maths: ": Maths,
        "Biology: ": Biology,
        "Computer Science: ": Computer_Science,
    }

    stds[Name]["Marks"] = Marks

    # SAVE
    save_students()
    print(f"\nSuccessfully saved {Name} to permanent storage!")