def main():

    # Get input from user
    greeting = input("Greeting: ")

    payout(greeting)


# Prints amount of money according to user text input
def payout(text):

    # Make input case-insensitive
    insensitive = text.lower().strip()

    if "hello" in insensitive:
        print("$0")
    elif insensitive.startswith('h'):
        print("$20")
    else:
        print("$100")

main()