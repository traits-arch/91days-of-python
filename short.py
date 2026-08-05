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
