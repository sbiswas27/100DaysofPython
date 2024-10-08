#Task: Let's try to create the hangman game in action! 
# Demo Link: https://appbrewery.github.io/python-day7-demo/

#create your word list

word_list = ["aardvark", "baboon", "camel"]

#choose a random word from the list
import random
chosen_word = random.choice(word_list)
#print(chosen_word)

#Assign 6 chances to the user to guess wrong
lives = 6

#Create a placeholder that could show the user how many letters the chosen word has
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#To start a while loop so that the user gets the chance to guess again, initialize a variable for the while condition

game_over = False

# A blank list to hold all the correct letters that the user guessed so that it can be displayed every time the user guesses a new letter
correct_letters = []


while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
  
    guess = input("Guess a letter: ").lower()

  # If the user enters a letter they have already guessed, no lives will be deducted
    if guess in correct_letters:
        print(f"You have already entered the {guess} in a previous try.")
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
      
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}. YOU LOSE**********************")
    
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

  
    print(stages[lives])



