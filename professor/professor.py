import random
import sys


def main():

    # Ask user for valid level number
    level = get_level()

    # Create score variable
    score = 0

    # Ask user for exactly 10 math questions
    for _ in range(10):

        # Create & reset fail counter every iteration
        fail = 0

        # Generate two random numbers every iteration according to level
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                # Check if user failed three times in a row
                if fail == 3:

                    # If so print out correct result and break out of the loop
                    print(f"{x} + {y} =", x + y)
                    break

                # Re-prompt user for number
                question = int(input(f"{x} + {y} = "))

                # Add one to score if it is correct and break out
                if x + y == question:
                    score += 1
                    break
                else:
                    # If number given by user is incorrect add one to fail counter
                    print("EEE")
                    fail += 1

            # If input given by user isn't integer add one to fail counter
            except ValueError:
                print("EEE")
                fail += 1
                pass

    # Print result score accomplished by user
    print("Score:", score)
    sys.exit(0)


def get_level():

    while True:
        try:
            # Re-prompts user for valid level integer
            ask = int(input("Level: "))

            if 1 <= ask <= 3:
                return ask

        except ValueError:
            pass


def generate_integer(level):
    try:
        if level == 1:
            x = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
    except ValueError:
        pass

    return x


if __name__ == "__main__":
    main()
