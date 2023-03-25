import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if find := re.search(r"^(\d+\.){3}\d+$", ip):
        ip_numbers = ip.split(".")
        for numbers in ip_numbers:
            if int(numbers) > 255:
                return False
            if len(numbers) > 1 and numbers.startswith("0"):
                return False
        return True
    return False


if __name__ == "__main__":
    main()