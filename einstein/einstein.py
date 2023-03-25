# Count energy value using Einstein Formula
def formula(value):

    # Count squared speed of light
    light = pow(300000000, 2)

    # Count energy and return it
    einstein = value * light
    return einstein


def main():

    # Get value of mass from user as integer
    mass = int(input("m: "))

    # Save result to variable and print it
    energy = formula(mass)
    print("E:", energy)

main()