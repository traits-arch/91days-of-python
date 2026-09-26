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
        if b_book in avl_books:
            print (f"{b_book} is added into cart")
            avl_books
        else:
            print ("The book you're looking for is currently not available")
    elif choice == 2:
        r_book = input("Please Enter the name of the book: " )
        avl_books[""] = ["Sugar Acid"]