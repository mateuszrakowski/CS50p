import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'"https?://(?:www\.)?youtube\.com/embed/(\w+)"', s, re.IGNORECASE):
        return f"https://youtu.be/{matches[1]}"
    return "None"

if __name__ == "__main__":
    main()