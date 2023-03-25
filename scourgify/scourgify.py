import sys
import csv


def main():

    # Check if CLI arguments are valid (2 arguments with .csv file names)
    first, second = check_cli(sys.argv)

    # Change columns inside given .csv file
    scourgify(first, second)


def check_cli(arguments):

    # Check CLI arguments, return only valid
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    if len(arguments) == 3:
        if arguments[1].endswith(".csv") and arguments[2].endswith(".csv"):
            return arguments[1], arguments[2]
        else:
            sys.exit("Not a CSV file")


def scourgify(input, output):

    # Create temporary list to store data with dictionaries per row
    temp = []

    try:
        # Save every row to temporary list
        with open(input) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                temp.append(row)
    # Handle error if file doesn't exist
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

    with open(output, "w") as csv_output_file:
        # Assign accurate fieldnames and create headers for each column
        writer = csv.DictWriter(csv_output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        # Unpack the two values from previous column "name" and assign it to new created columns
        # Write data to new CSV file
        for row in temp:
            last, first = row["name"].split(",")
            writer.writerow({"first":first.strip(), "last":last, "house":row["house"]})


if __name__ == "__main__":
    main()
