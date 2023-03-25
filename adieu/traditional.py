def main():

    yieu = farewell("Name: ")
    print("\nAdieu, adieu, to " + yieu)


def farewell(prompt):

    # Create list variable to store names
    names = []

    # Re-prompt user for names
    while True:
        try:
            ask = input(prompt)

            # Store names in a list
            names.append(ask)

        # Stop asking for names if CTRL+D
        except EOFError:
            break

    # Count total names added by user
    total = len(names)
    goodbye = ""

    # Return everyone names
    # If only one name is present
    if total < 2:
        return names[0]

    # If more than one name is present
    for name in names:
        if name != names[total - 1]:
            goodbye += f"{name}, "
        else:
            goodbye += f"and {name}"

    return goodbye


if __name__ == "__main__":
    main()