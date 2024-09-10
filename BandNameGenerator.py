#Task: Create a greeting for your program.Ask the user for the city that they grew up in and store it in a variable. Ask the user for the name of a pet and store it in a variable. Combine the name of their city and pet and show them their band name.

#Ask user for their name
user_name=input("Enter your name:\n")

#Greetings to user
print("Hello " + user_name)

#Ask user for their city
city_name=input("Enter the city you grew up:\n")

#Ask user for their pet name
pet_name=input("Enter the name of your pet:\n")

#Concatenate all the user inputs to get the band name
band_name=city_name + " " + pet_name

print("Your band name could be "+ band_name)
