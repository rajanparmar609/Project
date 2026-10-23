
import random

print("\n===== ROCK PAPER SCISSORS GAME =====\n")

name = input("Enter your name: ")

player_score = 0
computer_score = 0
tie_score = 0

while True:
    print("\nChoose your option:")
    print("A: Rock")
    print("B: Paper")
    print("C: Scissors")

    option = input("Enter your option: ").lower().strip()

    if option == "a":
        player = "rock"
    elif option == "b":
        player = "paper"
    elif option == "c":
        player = "scissors"
    else:
        print("Invalid option! Please enter A, B, or C.")
        continue

    comp = random.choice(["rock", "paper", "scissors"])

    print(f"\n{name} chose: {player.capitalize()}")
    print(f"Computer chose: {comp.capitalize()}")

    if player == comp:
        print("🤝 It's a tie!")
        tie_score += 1

    elif (
        (player == "rock" and comp == "scissors")
        or (player == "paper" and comp == "rock")
        or (player == "scissors" and comp == "paper")
    ):
        print(f"🎉 {name} wins this round!")
        player_score += 1

    else:
        print("🖥️ Computer wins this round!")
        computer_score += 1

    # Display the current score
    print("\n===== CURRENT SCORE =====")
    print(f"{name}: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {tie_score}")

    # Ask the user whether to play again
    again = input("\nDo you want to play one more time? (yes/no): ")
    again = again.lower().strip()

    if again not in ["yes", "y"]:
        break

# Final result
print("\n===== FINAL SCORE =====")
print(f"{name}: {player_score}")
print(f"Computer: {computer_score}")
print(f"Ties: {tie_score}")

if player_score > computer_score:
    print(f"\n🏆 Congratulations, {name}! You won the game!")
elif computer_score > player_score:
    print("\n🖥️ The computer won the game!")
else:
    print("\n🤝 The game ended in a tie!")

print("\nThanks for playing!")
