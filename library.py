import time
avl_books =  {"Anon": "The Silent patient", "Nemmo": "Lock Every Door", "Carter": "Fire In The Woods" }
avl_items = list(avl_books.items())
while True:
    print("--Welcome to the library Page--")
    print("Loading.... ")
    time.sleep(1)
    print("~~ Choose One of The options or enter 'q' to quit. ~~")
    print(" 1. Borrow a book \n 2. Return A Book \n 3. Search for a specific book. \n 4. List all Books available.")
    choice = int(input("Enter your Choice: "))
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
        avl_books[auth] = r_book
    elif choice == 3:
        s_book= input(str("Enter the Name of the book: "))
        if s_book in avl_books:
            add =input(f"{s_book} found, do you want to add it to the cart? (y/n").lower
            if add == "y":
                print("Book added to the cart")
            else:
                print("Book not added")
        else:
            search = ("Book not found, Want to search again? (y/n)")
            if search == "y":
                pass
            else: break
    elif choice == 4:
        for key, value in avl_books.items():
            print(f"Author: {key}, Book: {value}")
    elif choice == "q":
        break
    else: 
        print ("Invaild Choice detected, Please choose between 1-4")
        pass
