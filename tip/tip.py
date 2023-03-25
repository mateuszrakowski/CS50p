def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    delete_dollar = d.replace("$", "")
    convert = float(delete_dollar)
    float_value = round(convert, 1)

    return float_value


def percent_to_float(p):
    delete_sign = p.replace("%", "")
    percent = float(delete_sign) / 100

    return percent


main()