import random


def play_round():
    """Play one round and return the score earned."""
    secret = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("\n" + "=" * 40)
    print("        NUMBER GUESSING GAME")
    print("=" * 40)
    print("Range: 1 to 100")
    print(f"Attempts available: {max_attempts}")

    while attempts < max_attempts:
        remaining = max_attempts - attempts

        while True:
            raw = input(f"\nEnter your guess ({remaining} left): ").strip()
            try:
                guess = int(raw)
            except ValueError:
                print("Please enter a whole number from 1 to 100.")
                continue

            if not 1 <= guess <= 100:
                print("Please enter a number between 1 and 100.")
                continue
            break

        attempts += 1

        if guess == secret:
            score = max(100 - (attempts - 1) * 10, 10)
            print(f"\nCorrect! You guessed the number in {attempts} attempt(s).")
            print(f"Score for this round: {score}")
            return score

        if guess < secret:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    print(f"\nOut of attempts! The secret number was {secret}.")
    print("Score for this round: 0")
    return 0


def main():
    total_score = 0
    rounds = 0

    print("\nWELCOME TO THE NUMBER GUESSING GAME!")
    print("Guess the secret number between 1 and 100.")

    while True:
        rounds += 1
        total_score += play_round()

        print(f"\nTotal Score: {total_score}")
        print(f"Rounds Played: {rounds}")

        while True:
            again = input("\nPlay another round? (y/n): ").strip().lower()
            if again in ("y", "n"):
                break
            print("Please enter y for yes or n for no.")

        if again == "n":
            break

    print("\n" + "=" * 40)
    print("              GAME OVER")
    print("=" * 40)
    print(f"Rounds Played : {rounds}")
    print(f"Total Score   : {total_score}")
    print("Thank you for playing!")


if __name__ == "__main__":
    main()