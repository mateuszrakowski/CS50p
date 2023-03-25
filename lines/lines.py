import sys


def main():

    # Check if command arguments are valid & return number of lines with code
    lines = check_cli(sys.argv)
    print(lines)


def check_cli(arguments):

    # Conditionals to check if CLI are valid
    if len(arguments) == 1:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    if arguments[1].endswith(".py"):
        try:
            lines = count_lines(arguments[1])
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

    return lines


def count_lines(name):

    # Create variable to store number of code lines
    counter = 0

    with open(name) as file:
        # Iterate through lines in file
        for line in file:
            # Handle comments inside file
            if line.lstrip().startswith("# "):
                continue
            # Handle empty lines inside file
            elif line.isspace():
                continue
            # Add one to counter if line is code-only
            else:
                counter += 1

    return counter


if __name__ == "__main__":
    main()
