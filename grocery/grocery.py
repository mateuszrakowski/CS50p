def main():

    groceries("")


# Stores prompts from user, counts them and prints out
def groceries(prompt):

    # Create dictionary to store items and quantity
    groceries_list = {}

    while True:

        # Re-asks user for shopping items
        try:
            veggie = input(prompt)

            # Adds additional item to total number if it already exists
            if veggie in groceries_list:
                groceries_list[veggie] += 1

            # Stores a new prompted item and sets it's amount to 1
            else:
                groceries_list[veggie] = 1

        # Handles exit of the loop by user
        except EOFError:
            break

    # Printing newline for better transparency
    print("")

    # Iterates by dictionary, sorting it by keys and printing out with values
    for k, v in sorted(groceries_list.items()):
        print(v, k.upper())

main()