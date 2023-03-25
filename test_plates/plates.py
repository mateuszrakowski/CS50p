def main():

    # Get input from user with plates name
    plate = input("Plate: ")

    # Check and print statement
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Create empty list as variable
    c_list = []

    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check for special characters
    for character in s:
        if not character.isalnum():
            return False

    # Store characters in list
    for character in s:
        c_list.append(character)

    # Check if first 2 characters are letters
    if not c_list[0].isalpha() or not c_list[1].isalpha():
        return False

    # Check for digits inside plates
    for c in range(len(c_list) - 1):
        if c_list[c].isdigit() and c_list[c+1].isalpha():
            return False

    # Check if first used digit is "0"
    for c in range(len(c_list) - 1):
        if c_list[c] == "0" and c_list[c+1].isdigit():
            return False

    return True


if __name__ == "__main__":
    main()