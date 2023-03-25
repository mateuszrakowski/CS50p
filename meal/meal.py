def main():

    # Get input hour time from user
    time = input("What time is it? ")

    meal = convert(time)

    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")


def convert(time):

    # Split time to hours and minutes and convert them to float values
    x, y = time.split(":")
    minutes = float(y) / 60

    return float(x) + float(minutes)


if __name__ == "__main__":
    main()