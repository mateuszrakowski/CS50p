months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():

    outdated("Date: ")


def outdated(prompt):

    while True:

        # Re-ask user for correct date
        try:
            ask = input(prompt)

            # Replace signs to store date components in variables
            convert = ask.replace(",", "").replace("/", " ")

            # Store components as corresponding variables
            month, day, year = convert.split()

            # Add prefix "0" to months/days if needed
            if len(month) == 1:
                month = f"0{month}"
            if len(day) == 1:
                day = f"0{day}"

            # Validate correct number of days and assign type of schema to conditions
            if 1 <= int(day) <= 31:

                # Look up if month name is correct and "," is present
                # Could be upgraded in the future, condition doesn't check where "," sign is
                if "," in ask and month in months:
                    return print(f"{year}-{months[month]}-{day}")

                # Check if number of month is valid
                elif month.isdigit() and (1 <= int(month) <= 12):
                    return print(f"{year}-{month}-{day}")

        # Handles name errors, returns to start of the loop
        except NameError:
            pass

        # Handles value errors, returns to start of the loop
        except ValueError:
            pass


main()