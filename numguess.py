import time
import random
print("Welcome to the number guessing game!")
time.sleep(1)
print("A number between 1 and 100 has been chosen.")
time.sleep(1)
print("You have 7 attempts to guess the number.")
time.sleep(1)
print("But dont worry you'll get hints if you are wrong")
num= random.randint(1, 100)
attempts=7
while attempts>0:
        guess= int(input("Enter your guess: "))
        if guess==num:
         print("Congratulations! You have guessed the number correctly.")
         break
        else:
            if guess<num:
              print("Your guess is too low. Try again.")
            else:
              if guess>num:
                 print("Your guess is too high. Try again.")
              attempts -= 1
        time.sleep(1)
        print(f"You have {attempts} attempts left.\n")
        if attempts==0:
          print(f"Sorry, you have run out of attempts. But yk what , I still will tell u the number chosen.")
          time.sleep(1)
          print("It was", num)
feedback= input("Did you like the game? (yes/no): ")
if feedback.lower() == "yes":
   print("I'm very glad, I hope you would wanna play again soon!")
else:
  print("Ehh, I will try to make it better next time")
  time.sleep(2)
  print("But you know what, I dont really care......\nCoz thats a skill issue froom your side")
