import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    lower = 1
    upper = 100
    number_to_guess = random.randint(lower, upper)
    attempts = 7

    print(f"I'm thinking of a number between {lower} and {upper}.")
    print(f"You have {attempts} attempts to guess it.")

    for i in range(attempts):
        try:
            guess = int(input(f"\nAttempt {i+1}: Enter your guess: "))
            if guess < lower or guess > upper:
                print(f"Please guess a number between {lower} and {upper}.")
                continue

            if guess == number_to_guess:
                print("🎉 Congratulations! You guessed the correct number!")
                break
            elif guess < number_to_guess:
                print("📉 Too low. Try a higher number.")
            else:
                print("📈 Too high. Try a lower number.")
        except ValueError:
            print("🚫 Invalid input. Please enter a number.")

    else:
        print(f"\n❌ You've run out of attempts. The number was {number_to_guess}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
