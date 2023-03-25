from validator_collection import checkers


def main():
    print(email_validator(input("What's your email adress? ")))


def email_validator(s):
    if checkers.is_email(s):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()
