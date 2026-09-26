import time
avl_books =  {"Anon": "The silent patient", "Anon": "Lock Every Door", "Anon": "Fire In The Woods" }
while True:
    print("--Welcome to the library Page--")
    print("Loading.... ")
    time.sleep(1)
    print("~~ Choose One of The options or enter 'q' to quit. ~~")
    print("   1. Borrow a book \n 2. Return A Book \n 3. Search for a specific book. \n 4. List all Books available.")
    choice = input("Enter your Choice: ")
    if choice == 1:
        b_book = input(str("Enter the name of the book You want to borrow: "))
        auth = "Anon"
        auth= input("Name of the Author (if you have): ")
        if b_book in avl_books:
            print (f"{b_book} is added into cart")
            avl_books.pop(b_book)
        else:
            print ("The book you're looking for is currently not available")
    elif choice == 2:
        auth = "Anon"
        r_book = input("Please Enter the name of the book: " )
        auth = input ("Enter the name of the Author: ")
        avl_books[auth] = [r_book]