def main():

    # Get input from user
    camel = input("CamelCase: ")

    # Convert to snake case
    output = snake(camel)

    print("Snake_case: " + output)


def snake(camelCase):

    snakeCase = ""

    # Find every upletter character and convert it to camel case
    for _ in camelCase:
        if _.isupper():
            snakeCase += "_" + _.lower()
        else:
            snakeCase += _

    return snakeCase


main()