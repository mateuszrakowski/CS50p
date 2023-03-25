from pyfiglet import Figlet
import random
import sys


def main():

    txt = convert("Input: ")
    print(txt)


def convert(prompt):

    # Check if number of arguments is valid
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")

    # Store list of fonts in variable
    f = Figlet()
    font_list = f.getFonts()

    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        if sys.argv[2] not in font_list:
            sys.exit("Invalid usage")

    # Prompt user for input text to convert
    ask = input(prompt)

    # If user didn't add arguments print random font
    if len(sys.argv) == 1:
        random_font = random.choice(font_list)
        f.setFont(font=random_font)
        output = f.renderText(ask)
        return output

    # Check if argument is valid and font name is correct
    f.setFont(font=sys.argv[2])
    output = f.renderText(ask)
    return output


main()
