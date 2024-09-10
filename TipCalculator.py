# Task: We're going to build a tip calculator.If the bill was $150.00, split between 5 people, with 12% tip.Each person should pay:(150.00 / 5) * 1.12 = 33.6. After formatting the result to 2 decimal places = 33.60

#Welcome Greetings
print("Welcome to the tip calculator!")

#Input the Bill amount
bill = float(input("What was the total bill? $"))

#Input the tip percentage
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

#Input the no. of people to split the bill
people = int(input("How many people to split the bill? "))

#Calculating the final payment value
payment= round(((bill / people) * (1+tip/100)),2)


print (f"Each person should pay: {payment}")
