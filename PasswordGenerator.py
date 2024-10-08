#Task:  Generate a user personalized password
# Demo Link: https://appbrewery.github.io/python-day5-demo/

import random
#build the datasets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Ask for user input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password=""
password_list=[]
for i in range(0,nr_letters):
    password_list.append(random.choice(letters))
for i in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
for i in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
for i in password_list:
    password +=i
print(f"Your password is : {password}")
