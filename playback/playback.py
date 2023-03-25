# Get text input from user
text = input()

# Strip whitespaces on beginning and end of the string
stripped = text.strip()

# Replace whitespaces between words
playback = stripped.replace(" ", "...")

print(playback)