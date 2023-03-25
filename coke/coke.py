def main():

    # Insert accepted coin to the machine
    change = value()

    print(f"Change Owed: {change}")


def value():

    due = 50
    coins = [25, 10, 5]

    # While price of one bottle is not paid ask customer for more coins
    while due > 0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))

        # Check if coin is valid and modify the due value
        if coin in coins:
            due -= coin

    return abs(due)


main()