import random


def main():

    result = game("Level: ")
    print(result)


def game(prompt):

    while True:

        # Re-prompt user for valid level value
        try:
            level = int(input(prompt))

            # If input is correct resume
            if level > 0:
                break

        # Handle incorrect input of non-integer values
        except ValueError:
            pass

    # Pick random integer from a set of numbers
    drawn = random.randint(1, level)

    while True:

        # Re-prompt user for valid guess value
        try:
            guess = int(input("Guess: "))

            # Handle incorrect values
            # Return information about game state
            if guess <= 0:
                pass
            elif guess > drawn:
                print("Too large!")
                pass
            elif guess < drawn:
                print("Too small!")
                pass
            else:
                return "Just right!"

        # Handle incorrect input of non-integer values
        except ValueError:
            pass


if __name__ == "__main__":
    main()
