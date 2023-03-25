meals = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():

    taqueria("Item: ")


def taqueria(prompt):

    # Create variable to store bill value
    total = 0

    # Re-ask customer for meal name and return total bill in dollars
    while True:
        try:
            # Re-ask and convert string to titlecased
            meal = input(prompt).title()

            # Lookup if given meal name is present in menu
            if meal in meals:

                # Add meal price to customer total bill and print it
                total += float(meals[meal])
                print(f"Total: ${total:.2f}")

        # Handles CTRL-D printing errors to stop the program, also prints pretty newline
        except EOFError:
            print("")
            break


main()