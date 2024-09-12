# Define a funtion to calculate the compatibility between two names 
# how many times the letters in word 'TRUE' appear in the names and how many times letters in 'LOVE' appears in the name and then combine them. That's the compatibility score! 
def calculate_love_score(name1, name2):
    total1=0
    for letter in 'TRUE':
        for char in name1.upper():
            if letter == char:
                total1 +=1
        for char in name2.upper():
            if letter == char:
                total1 += 1

    total2=0
    for letter in 'LOVE':
        for char in name1.upper():
            if letter == char:
                total2 += 1
        for char in name2.upper():
            if letter == char:
                total2 += 1

    print(f"{total1}{total2}")
    
calculate_love_score("Kanye West", "Kim Kardashian")
