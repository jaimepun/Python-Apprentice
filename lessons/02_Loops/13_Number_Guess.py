
import random
from itertools import count

number = random.randint(0,100)
# Pick the random number
for i in count ():
    response=input ("guess a number between 1 to 100  ")
    response=int(response)
    if number==response:
        print ("correct!")
        break
    elif number>response:print ("The guess is too low")
    elif number<response:print ("the guess is too high")
    else: print ("that is not a number")
    # Get the user's guess


    # If the user's guess is too high, tell the user
    # If the user's guess is too low, tell the user
    # If the user's guess is correct, tell the user and break out of the loop


