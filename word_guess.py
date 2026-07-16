import time
import random
print("Welcome to the word guessing game")
time.sleep(1)
print("Here, you'll have a hint on the first letter\n And you have to guess the left")
time.sleep(1)
print("But remember, You only have limited attempts")
time.sleep(1)
name= input("Whats your name: ")
print("Good luck !!",name)

words = ["berries","liquid","python","ribbon","doorknob","crayon","arcade","portable"]
word = random.choice(words)
time.sleep(1)
Guesses= ""
attempts= 12

while attempts > 0:
    failed = 0

    for char in word:
        if char in Guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    # checking if the guess is correct already
    if failed == 0:
        print("You win...")
        time.sleep(2)
        print("The word is: ", word)
        break

    # taking the input
    guess = input("Enter your guess: ").lower()

    # validating it
    if len(guess) != 1 or not guess.isalpha():
        print("Not a valid input...")
        time.sleep(1)
        print("Please make sure you're only using alphabetical characters\n.......\nOne at a time")
        continue
    if guess in Guesses:
        print("You have already guessed that character")
        continue
    Guesses += guess
    if guess not in word:
        print ("You have guessed the wrong character")
        print("A wasted attempt")
        time.sleep(1)
        attempts -= 1
        print("You have",attempts," left")

        if attempts==0:
            print("You ran out of attempts")
            time.sleep(1)
            print("Game over, You lose")
            time.sleep(2)
            print("The word was: ",word)


 




