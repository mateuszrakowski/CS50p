def main():

    # Get input from user
    name = input("File name: ")

    extensions(name)


def extensions(text):

    # Make input case-insensitive
    insensitive = text.lower().strip()

    if insensitive.endswith(".jpg") or insensitive.endswith(".jpeg"):
        print("image/jpeg")
    elif insensitive.endswith(".gif"):
        print("image/gif")
    elif insensitive.endswith(".png"):
        print("image/png")
    elif insensitive.endswith(".pdf"):
        print("application/pdf")
    elif insensitive.endswith(".zip"):
        print("application/zip")
    elif insensitive.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")


main()