import random
import os
from hangman_words import animals, brands, countries, alphabet
from hangman_art import logo, stages

print(logo)

category_picked = False
already_guessed_wrong = []
end_of_game = False
lives = 6

#User picks a word category
while not category_picked:
    category = input("""Select a category -
'A' for Animals
'B' for Brands
'C' for Countries\n""").lower()
    if category == "a":
        chosen_word = random.choice(animals)
        chosen_category = "Animals"
        category_picked = True
    elif category == "b":
        chosen_word = random.choice(brands)
        chosen_category = "Brands"
        category_picked = True
    elif category == "c":
        chosen_word = random.choice(countries)
        chosen_category = "Countries"
        category_picked = True
    os.system('clear')
    print(logo)
print(f"You've chosen {chosen_category}. You have 6 guesses.")

word_length = len(chosen_word)

#Create blanks
display = []
for letter in range(word_length):
    display.append("_")

while not end_of_game:
    #Check if user guess is a letter of alphabet
    guess_valid = False
    while not guess_valid:
        guess = input("\nGuess a letter: ").lower()
        if guess.isalpha():  #Check if guess is a letter
            guess_valid = True

    #Clear console
    os.system('clear')
    print(logo)
    print(f"Category: {chosen_category}.\n")

    if guess in display:
        print(f"You've already guessed {guess}\n")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        if guess not in already_guessed_wrong:
            lives -= 1
            already_guessed_wrong.append(guess)
            print(f"You guessed {guess}, that's not in the word. You've got {lives} lives left.\n")
        else:
            print(f"You've already guessed {guess}, that's not in the word.\n")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")
    print(f"Wrong guesses: {', '.join(already_guessed_wrong)}\n")

    #Print ASCII art
    print(stages[lives])

    #Check if user has got all letters/ran out of lives
    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print(f"You lost! The correct word was {chosen_word}")
