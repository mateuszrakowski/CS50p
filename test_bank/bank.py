def main():

    # Get input from user
    greeting = input("Greeting: ")

    print(value(greeting))


# Prints amount of money according to user text input
def value(greeting):

    # Make input case-insensitive
    converted = greeting.lower().strip()

    if "hello" in converted:
        return 0
    elif converted.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
