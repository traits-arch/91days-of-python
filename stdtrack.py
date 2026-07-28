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

def std_avg(Student):
        if Student in stds:
                marks = stds[Student]["Marks"]
                total = 0
                count = 0
                for subject, score in marks.items():
                        if score != "N/A":
                         total += score
                        count += 1
                if count > 0:
                        avg = total / count
                        print(f"The average marks for {Student} is: {avg:.2f}")
                        stds[Student]["Average"]= avg
                else:
                        print("No valid numerical marks found.")
        else:
                print("Student not found.")
def dash():
    time.sleep(0.5)
    print("\n-----Welcome to Student Dashboard-----")
    time.sleep(0.5)
    print("Choose one of the options: ")
    print(
        "1. Add a Student\n2. Check Average\n3. Find a student\n4. Show All\n5. Find the topper\n6. Exit"
    )

    try:
        option = int(input("Choose one(1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if option == 1:
        name = input("Enter the name of the student: ")
        std_add(name)
    elif option == 2:
        Student = str(input("Name of the student: "))
        std_avg(Student)
    elif option == 3:
        Student = str(input("Name of the student: "))
        if Student in stds:
            print(f"Student {Student} is found!")
            print(json.dumps(stds[Student], indent=2))
        else:
            print("Student not found.")
    elif option == 4:
        print("\n--- All Students ---")
        print(json.dumps(stds, indent=2))
    elif option == 5:
        stds["Average"]
    elif option == 6:
        print("Goodbye!")
        exit()
    else:
        print("Invalid input, Please choose between (1-6)")


# Loop to continuously run the dashboard until you want to stop
while True:
    dash()
    sarg = input("\n(a) Repeat or (b) Exit: ").lower()
    if sarg != "a":
        print("Exiting Program. All data safely saved!")
        break