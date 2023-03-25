import emoji


def main():
    output = emojize("Input: ")
    print("Output:", output)


def emojize(prompt):
    ask = input(prompt)
    return emoji.emojize(ask, language="alias")


main()
