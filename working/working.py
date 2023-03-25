import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Find & validate correct 12-hours format
    if matches := re.search(
        r"^([1-9][0-9]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-9]?):?([0-5][0-9])? (AM|PM)$",
        s,
    ):
        # Divide input to two pieces and store hours in variables
        first_part, second_part = s.split("to")
        st_hour = int(matches[1])
        nd_hour = int(matches[4])

        # Convert PM to 24-hours format and take care of exception in PM (12 PM = 12:00)
        if "PM" in first_part:
            if matches[1] != "12":
                st_hour += 12
        if "PM" in second_part:
            if matches[4] != "12":
                nd_hour += 12

        # Take care of exception in AM (12 AM == 00:00)
        if "AM" in first_part:
            if matches[1] == "12":
                st_hour = 00
        if "AM" in second_part:
            if matches[4] == "12":
                nd_hour = 00

        # Check if hours are valid
        if int(matches[1]) < 13 and int(matches[4]) < 13:
            # Check if minutes are present in input (handles TypeError)
            if matches[2] != None and matches[5] != None:
                # Check if minutes are valid
                if int(matches[2]) < 60 and int(matches[5]) < 60:
                    # Return 24-hour format with minutes
                    return f"{st_hour:02}:{matches[2]} to {nd_hour:02}:{matches[5]}"
            # Return 24-hour format with full hours
            return f"{st_hour:02}:00 to {nd_hour:02}:00"

    # Raise error according to task instructions
    raise ValueError


if __name__ == "__main__":
    main()
