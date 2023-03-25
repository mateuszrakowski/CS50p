import inflect

def main():

    yieu = farewell("Name: ")
    print("\nAdieu, adieu, to " + yieu)


def farewell(prompt):

    p = inflect.engine()

    # Create variable to store names
    mylist = []

    # Re-prompt user for names
    while True:
        try:
            ask = input(prompt)

            # Append every name to list variable
            mylist.append(ask)

        # Stop asking for names if CTRL+D
        except EOFError:
            break

    # Returns output as a string with "and" present before last list element
    output = p.join((mylist))
    return output


if __name__ == "__main__":
    main()