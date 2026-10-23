
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 7

    print("===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it!")

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        if guess < 1 or guess > 100:
            print("Hint: Enter a number between 1 and 100.")
            continue

        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break

        difference = abs(secret_number - guess)

        if guess < secret_number:
            print("Hint: Your guess is too LOW!")
        else:
            print("Hint: Your guess is too HIGH!")

        if difference <= 5:
            print("🔥 Very close to the number!")
        elif difference <= 10:
            print("😊 You are getting closer!")
        elif difference <= 20:
            print("🙂 You are somewhat close!")
        else:
            print("❄️ You are far away from the number!")

        attempts -= 1

    else:
        print("\nGame Over! You used all your attempts.")
        print(f"The correct number was {secret_number}.")

guessing_game()
