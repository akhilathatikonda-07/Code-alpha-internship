import random

# Predefined words
words = ["python", "computer", "hangman", "program", "developer"]

# Select random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Variables
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

print("=== HANGMAN GAME ===")

# Game loop
while incorrect_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_guesses - incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    # User input
    guess = input("Enter a letter: ").lower()

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    # Wrong guess
    else:
        print("Wrong Guess!")
        incorrect_guesses += 1

# Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)