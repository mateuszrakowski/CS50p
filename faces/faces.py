# Convert input string with according emotes
def convert(text):
    emoji = text.replace(":)", "🙂").replace(":(", "🙁")
    print(emoji)

def main():

    # Get text input from user
    text = input("Text Your message! \n")

    # Convert string with emojis
    convert(text)

main()