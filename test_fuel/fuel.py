def main():

    ask = input("Fraction: ")
    fraction = convert(ask)
    print(gauge(fraction))


def convert(prompt):

    # Re-ask user for correct value of fuel
    # Split string input and divide values as ints to return rounded value of fuel
    x, z = prompt.split("/")

    value = round(int(x) / int(z) * 100)

    return value


def gauge(percentage):

    # Handles 99-100% values
    if 99 <= percentage <= 100:
        return "F"

    # Handles 0-1% values
    elif 0 <= percentage <= 1:
        return "E"

    # Handle only correct values in range
    elif 2 < percentage < 98:
        return f"{percentage}%"

    else:
        return "Wrong fraction number"


if __name__ == "__main__":
    main()