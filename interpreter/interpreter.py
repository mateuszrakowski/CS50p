def main():

    # Get input from user
    numbers = input("Expression: ")

    result = calculate(numbers)
    print(f"{result:.1f}")


def calculate(n):

    # Split and save arguments to separate variables
    x, y, z = n.strip().split()

    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        return float(x) / float(z)


main()