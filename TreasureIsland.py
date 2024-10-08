# Task: Build a "Chose your own adventure game".
# Demo Link - https://appbrewery.github.io/python-day3-demo/

#Greetings for the user
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Input decisions for user and plan your game accordingly (as you like!)

decision = input("Do you want to go left or right?")

if decision =='right' or decision == 'Right':
   print("Sorry, Game Over!")
else:
   decision = input("Do you want to swim or wait?")
   if decision=='Swim' or decision=='swim':
       print("Sorry, Game Over!")
   else:
       decision=input("Which door would you want to open? Red,Yellow or Blue, Choose!")
       if decision=='Blue' or decision=='blue':
           print("Sorry, Game Over!")
       elif decision=='Red' or decision=='red':
           print("Sorry, Game Over!")
       else:
           print("Yay!! You Win!")
