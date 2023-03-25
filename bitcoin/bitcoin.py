import requests
import sys


def main():

    # Check and validate CLI arguments
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].isdigit() and float(sys.argv[1]) == ValueError:
        sys.exit("Command-line argument is not a number")

    # Retrieve one BTC value in USD
    btc_usd = bitcoin()

    # Calculate value for user
    output = btc_usd * float(sys.argv[1])

    # Return value of Bitcoins
    print(f"${output:,.4f}")


def bitcoin():

    # Query BitCoin API
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        result = r.json()

        # Nest inside JSON and retrieve value
        usd_value = result["bpi"]["USD"]["rate"]

    # Handle request errors
    except requests.RequestException:
        sys.exit("Request error - try again later")

    # Replace "," to convert string to float
    convert_float = usd_value.replace(",", "")

    return float(convert_float)


if __name__ == "__main__":
    main()