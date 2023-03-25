def main():

    # Get twitter post text
    post = input("Input: ")

    # Shorten the twitter post text
    print(f"Output: {shorten(post)}")


def shorten(word):

    shortened = ""
    vowels = ["a", "e", "i", "o", "u"]

    # Find vowels in text and skip them
    for character in word:
        if character.lower() not in vowels:
            shortened += character

    return shortened


if __name__ == "__main__":
    main()