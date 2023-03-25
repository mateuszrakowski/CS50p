def main():

    # Get input from user
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    answer(question)


# The knowledge function that returns answer according to input
def answer(text):

    # Lowercase text to make it case-insensitive
    insensitive = text.lower().strip()

    match insensitive:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()