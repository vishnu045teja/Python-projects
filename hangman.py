import random

# List of words to choose from
word_list = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'developer', 'programmer']

def choose_word():
    return random.choice(word_list)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(' '.join('_' for _ in word))
    print("\n")

    while len(word_letters) > 0 and tries > 0:
        # Get the user's guess
        guess = input('Guess a letter: ').lower()

        # Validate the guess
        if len(guess) != 1 or guess not in alphabet:
            print("Invalid input. Please enter a single letter from the alphabet.")
            continue
        elif guess in used_letters:
            print("You've already guessed that letter. Try again.")
            continue
        else:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print(f"Good guess: {guess} is in the word.")
            else:
                tries -= 1
                print(f"Wrong guess: {guess} is not in the word.")
        
        # Display the current progress
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print(display_hangman(tries))
        print(' '.join(word_display))
        print(f"Used letters: {', '.join(sorted(used_letters))}")
        print("\n")
    
    if tries == 0:
        print(f"Sorry, you lost! The word was '{word}'.")
    else:
        print(f"Congratulations! You guessed the word '{word}' correctly!")

if __name__ == "__main__":
    play_hangman()
