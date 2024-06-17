import random

def get_bot_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner_rps(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'scissors' and bot_choice == 'paper') or \
         (user_choice == 'paper' and bot_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_rps():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        bot_choice = get_bot_choice()
        print(f"Bot chose: {bot_choice}")
        
        result = determine_winner_rps(user_choice, bot_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing Rock, Paper, Scissors! Goodbye.")

def play_number_guess():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = input("Guess the number between 1 and 100: ")
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1
        
        if user_guess < number:
            print("Too low!")
        elif user_guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break
    
    print("Thanks for playing the Number Guessing Game! Goodbye.")

def play_dice_roll():
    print("Welcome to the Dice Rolling Game!")
    while True:
        roll = input("Press enter to roll the dice (or type 'quit' to stop): ")
        if roll.lower() == 'quit':
            break
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled a {dice1} and a {dice2}. Total: {dice1 + dice2}")

    print("Thanks for playing the Dice Rolling Game! Goodbye.")

def play_coin_toss():
    print("Welcome to the Coin Toss Game!")
    while True:
        user_choice = input("Guess the outcome (heads or tails): ").lower()
        if user_choice not in ['heads', 'tails']:
            print("Invalid choice. Please choose heads or tails.")
            continue

        outcome = random.choice(['heads', 'tails'])
        print(f"The coin landed on: {outcome}")
        
        if user_choice == outcome:
            print("You guessed it right!")
        else:
            print("Sorry, you guessed wrong.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing the Coin Toss Game! Goodbye.")

def play_word_scramble():
    print("Welcome to the Word Scramble Game!")
    words = [
        'python', 'chatbot', 'programming', 'developer', 'algorithm',
        'function', 'variable', 'condition', 'iteration', 'syntax',
        'compiler', 'interpreter', 'debugging', 'exception', 'inheritance',
        'polymorphism', 'encapsulation', 'abstraction', 'database', 'network',
        'security', 'encryption', 'decryption', 'interface', 'protocol'
    ]
    
    while True:
        word = random.choice(words)
        scrambled_word = ''.join(random.sample(word, len(word)))
        print(f"Scrambled word: {scrambled_word}")
        
        user_guess = input("Guess the word: ")
        
        if user_guess.lower() == word:
            print("Correct! Well done!")
        else:
            print(f"Sorry, the correct word was: {word}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing the Word Scramble Game! Goodbye.")

def main_menu():
    print("Welcome to the Game Hub!")
    while True:
        print("\nPlease choose a game to play:")
        print("1. Rock, Paper, Scissors")
        print("2. Number Guessing Game")
        print("3. Dice Rolling Game")
        print("4. Coin Toss Game")
        print("5. Word Scramble Game")
        print("6. Quit")
        
        choice = input("Enter the number of your choice: ").strip()
        
        if choice == '1':
            play_rps()
        elif choice == '2':
            play_number_guess()
        elif choice == '3':
            play_dice_roll()
        elif choice == '4':
            play_coin_toss()
        elif choice == '5':
            play_word_scramble()
        elif choice == '6':
            print("Thanks for visiting the Game Hub! Goodbye.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main_menu()
