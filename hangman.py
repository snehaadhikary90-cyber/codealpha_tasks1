
import random

# Step 1: Store 5 predefined words in a list
words = ["python", "apple", "tiger", "train", "chair"]

# Step 2: Select a random word
word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")

# Step 4: Start the game
while wrong_guesses < max_attempts:

    # Display guessed and hidden letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses remaining:", max_attempts - wrong_guesses)

    # Check whether the player has guessed the entire word
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    # Take input from the player
    guess = input("Enter a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    # Check whether the guessed letter is correct
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Step 5: Display the final result
if wrong_guesses == max_attempts:
    print("\nGame Over! You have used all your attempts.")
    print("The correct word was:", word)
