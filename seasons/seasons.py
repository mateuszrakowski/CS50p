from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    minutes_age = days_to_minutes(input("Date of Birth: "))
    print(minutes_age)


def days_to_minutes(s):
    # Converts the string input to datatime class object
    try:
        birth = date.fromisoformat(s)
    # Handles ValueError if format isn't valid (YYYY-MM-DD)
    except ValueError:
        sys.exit("Invalid date")

    # Gets and stores today date
    today = date.today()

    # Handles invalid birth date, that generates >0 values
    if birth > today:
        sys.exit("Invalid date")

    # Difference between today and birth date, stores number of days
    age = (today - birth).days

    # Counts the number of total minutes
    total_minutes = age * 24 * 60

    # Converts the total number of minutes from integer to text
    return f"{p.number_to_words(total_minutes, andword='')} minutes".capitalize()


if __name__ == "__main__":
    main()
