import sys
import csv


def main():

    # Check if CLI arguments are valid (2 arguments with .csv file names)
    first, second = check_cli(sys.argv)

    # Change columns inside given .csv file
    scourgify(first, second)


def check_cli(arguments):

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

    temp = []

    try:
        with open(input) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                temp.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

    converted = []

    for row in temp:
        last, first = row["name"].split(",")
        converted.append({"first":first.strip(), "last":last, "house":row["house"]})

    with open(output, "w") as csv_output_file:
        writer = csv.DictWriter(csv_output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in converted:
            writer.writerow(row)


if __name__ == "__main__":
    main()