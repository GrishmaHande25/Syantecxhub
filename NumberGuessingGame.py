import random

print("=== Number Guessing Game ===")

best_score = None

while True:
    # Difficulty selection
    print("\nSelect Difficulty:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        max_range = 50
    elif choice == '2':
        max_range = 100
    elif choice == '3':
        max_range = 200
    else:
        print("Invalid choice! Setting Medium level.")
        max_range = 100

    # Random number
    number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI chose a number between 1 and {max_range}. Start guessing!")

    # Game loop
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try higher.")
            elif guess > number:
                print("Too high! Try lower.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Enter a valid number!")

    # Best score check
    if best_score is None or attempts < best_score:
        best_score = attempts

    print("Best (lowest) attempts so far:", best_score)

    # Replay option
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
