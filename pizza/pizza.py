import sys
from tabulate import tabulate
import csv


def main():

    # Check if CLI argument is valid with given rules
    pizza_menu = check_cli(sys.argv)

    # Print grid table with headers as keys
    print(tabulate(pizza_menu, headers="keys", tablefmt="grid"))


def check_cli(arguments):

    # Conditionals to check for exact one argument with existing .csv format file
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    if len(arguments) == 2:
        if arguments[1].endswith(".csv"):
            try:
                output = menu(arguments[1])
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")

    return output


def menu(name):

    # Create empty list to store file rows as dictionaries
    pizzas = []

    with open(name) as csv_file:
        reader = csv.DictReader(csv_file)

        # Add every row as dictionary to list
        for row in reader:
            pizzas.append(row)

    return pizzas


if __name__ == "__main__":
    main()
