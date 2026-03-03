import random

# Word categories by difficulty
word_bank = {
    "easy": ["cat", "dog", "sun", "book", "tree"],
    "medium": ["python", "laptop", "garden", "coding", "school"],
    "hard": ["developer", "hangman", "computer", "internship", "programming"]
}


def choose_difficulty():
    while True:
        level = input("\nChoose difficulty (easy / medium / hard): ").lower()
        if level in word_bank:
            return level
        else:
            print("Invalid choice. Please select easy, medium, or hard.")


def play_game():
    level = choose_difficulty()
    chosen_word = random.choice(word_bank[level])

    if level == "easy":
        max_attempts = 8
    elif level == "medium":
        max_attempts = 6
    else:
        max_attempts = 4

    guessed_letters = []
    incorrect_guesses = 0

    print("\n🎮 Game Started!")
    print("_ " * len(chosen_word))

    while incorrect_guesses < max_attempts:

        guess = input("\nGuess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single valid alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("✅ Correct guess!")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

        # Display progress
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", ", ".join(guessed_letters))

        # Win check
        if all(letter in guessed_letters for letter in chosen_word):
            print("\n🎉 You won! The word was:", chosen_word)
            return

    print("\n💀 Game Over! The word was:", chosen_word)


# Main program loop (Replay feature)
print("🔥 Welcome to Advanced Hangman!")

while True:
    play_game()
    
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing! 👋")
        break