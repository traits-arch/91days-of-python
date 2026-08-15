#plaindrome play
while True: 
    palindrome= input("Enter a string: ").lower().replace(" ", "")
    if palindrome[::-1] == palindrome:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    ans1=input("Do you also wanna \n 1. Count the number of vowels in the string. \n 2. Count the number of consonants in the string. \n 3. Both. \n 4. None, Exit \n Choose an option (1-4): ")
    if ans1 == "1" or ans1 == "3":
        vowels = "aeiou"
        vowel_count = sum(1 for char in palindrome if char in vowels)
        print("The number of vowels in the string is:", vowel_count)
    if ans1 == "2" or ans1 == "3":
        consonants = "bcdfghjklmnpqrstvwxyz"
        consonant_count = sum(1 for char in palindrome if char in consonants)
        print("The number of consonants in the string is:", consonant_count)
    ans= input("Do you want to check another string? (Y/N): ").lower()
    if ans == 'n':
            break

#Expense Tracker
print("<<== Welcome to the Expense Tracker! ==>")
import time
time.sleep(1)
print("Initializing...")
time.sleep(1)
while True:
    print("1. Add an expense \n2. View expenses \n3. Exit")
    ans = input("Enter your choice (1-3): ")
    if ans == "1":
        expense = input("Enter the expense description: ")
        amount = float(input("Enter the expense amount: "))
        with open("expenses.txt", "a") as file:
            file.write(f"{expense}: ₹{amount:.2f}\n")
        print("Expense added successfully!\n")
    elif ans ==2:
        print("Expenses:")
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            if not expenses:
                print("No expenses recorded yet.\n")
            else:
                for expense in expenses:
                    print(expense.strip())
        print()
    elif ans == "3":
        print("Exiting the Expense Tracker. Goodbye!")
        break

#contacts book
print("<<== Welcome to the Contacts Book! ==>")
time.sleep(1)
while True:
    print("Choose an option: \n1. Add a contact \n2. Search contacts \n3. Show All \n4. Delete All \n5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        with open("contacts.txt", "a") as file:
            file.write(f"{name}: {phone}\n")
        print("Contact added successfully!\n")
    elif choice == "2":
        search_name = input("Enter the name to search: ")
        found = False
        with open("contacts.txt", "r") as file:
            for line in file:
                if search_name.lower() in line.lower():
                    print("Contact found:", line.strip())
                    found = True
                    break
        if not found:
            print("Contact not found.\n")
    elif choice == "3":
        print("All Contacts:")
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts recorded yet.\n")
            else:
                for contact in contacts:
                    print(contact.strip())
    elif choice == "4":
        confirm = input("Are you sure you want to delete all contacts? (Y/N): ").lower()
        if confirm == "y":
            open("contacts.txt", "w").close()  # Clear the file
            print("All contacts deleted successfully!\n")
        else:
            print("Deletion canceled.\n")
    elif choice == "5":
        print("Exiting the Contacts Book. Goodbye!")
        break
