import time #to add pauses between the instructions
import random #to generate a random number for the guessing game
print("Welcome to the number guessing game!")
time.sleep(1)# here is the pause
print("A number between 1 and 100 has been chosen.")
time.sleep(1)
print("You have 7 attempts to guess the number.")
time.sleep(1)
print("But dont worry you'll get hints if you are wrong")
num= random.randint(1, 100) # range of random number
attempts=7 # total number of attempts
while attempts>0: #keeps looping till attempts are 0
        guess= int(input("Enter your guess: "))
        if type(guess)!=int:
           print("Only numbers are allowed")
        if guess==num:
         print("Congratulations! You have guessed the number correctly.")
         break #stop when the right number is guessed 
        else:
            if guess<num:
              print("Your guess is too low. Try again.")
            else:
              if guess>num:
                 print("Your guess is too high. Try again.")
              attempts -= 1 #keeping track of attempts
        time.sleep(1)
        print(f"You have {attempts} attempts left.\n")
        if attempts==0: #game over
          print(f"Sorry, you have run out of attempts. But yk what , I still will tell u the number chosen.")
          time.sleep(1)
          print("It was", num)
feedback= input("Did you like the game? (yes/no): ") #ofc, feedback is neccessary, not that i care though
if feedback.lower() == "yes":
   print("I'm very glad, I hope you would wanna play again soon!")
else:
  
  print("Ehh, I will try to make it better next time")
  time.sleep(2)
  print("But you know what, I dont really care......\nCoz thats a skill issue froom your side")

#another game , but guessing words this time
print("Welcome to the next game")