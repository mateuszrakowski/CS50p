from PIL import Image, ImageOps
import sys


def main():

    # Checks given arguments and returns two arguments, the correct file names
    input_file, output_file = check_cli(sys.argv)

    # Overlays images to wear a CS50 shirt
    shirt(input_file, output_file)


def check_cli(arguments):

    # Store correct formats in a list
    formats = ["jpeg", "jpg", "png"]

    # Handle incorrect number of CLI arguments
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")

    # Split first argument to pull given file extension
    try:
        _, format = arguments[1].lower().split(".")
    # Handle arguments without file extension
    except ValueError:
        sys.exit("Invalid input")

    # Check if second argument extension is the same
    if format in formats:
        if arguments[2].lower().endswith(format):
            return arguments[1], arguments[2]
        # Otherwise exit with information
        else:
            sys.exit("Input and output have different extensions")
    sys.exit("Invalid input")


def shirt(input, output):

    # Handle error if file does not exist
    try:
        photo = Image.open(input)
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Open shirt img and get size of it in a tuple
    img = Image.open("shirt.png")
    size = img.size

    # Convert and fit image into shirt size
    muppet = ImageOps.fit(photo, size)

    # Overlay images
    muppet.paste(img, img)

    # Save output into a file with given name
    muppet.save(output)


if __name__ == "__main__":
    main()
