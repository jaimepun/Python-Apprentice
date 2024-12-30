
import random

def ask_integer(prompt):
  number= input ("try to guess the number I am thinking of /(the number is not divisible by 7)/ ")
      
  if number==(10):
            print("correct!")
  if number < (10):
    print ("the guess is too low. ")
    if number > (10):
        print ("the guess is too high. ")
  return int(input(prompt))
ask_integer
# Pick the random number

# In your loop:

    # Get the user's guess

    # If the user's guess is divisible by 7, tell the user to start over

    # If the user's guess is too high, tell the user
    # If the user's guess is too low, tell the user
    # If the user's guess is correct, tell the user and break out of the loop


