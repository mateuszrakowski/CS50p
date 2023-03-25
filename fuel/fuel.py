def main():

    fraction = fuel("Fraction: ")
    print(fraction)


def fuel(prompt):

    # Re-ask user for correct value of fuel
    while True:
        try:
            # Re-ask ask user till correct value is given
            ask = input(prompt)

            # Split string input and divide values as ints to return rounded value of fuel
            x, z = ask.split("/")
            value = round(int(x) / int(z) * 100)

            # Handles 99-100% values
            if 99 <= value <= 100:
                return "F"

            # Handles 0-1% values
            elif 0 <= value <= 1:
                return "E"

            # Handle only correct values in range
            elif 2 < value < 98:
                return f"{value}%"


        # Handles division by zero and returns to re-ask loop
        except ZeroDivisionError:
            pass

        # Handles values error like strings or float values and returns to re-ask loop
        except ValueError:
            pass


main()