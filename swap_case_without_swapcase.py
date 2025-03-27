# Get a string
text = input("String: ")

# Create an empty new string
swapped_text = ""

# Go through each letter
for char in text:
    # If it's uppercase, change it to lowercase
    if 'A' <= char <= 'Z':
        swapped_text += chr(ord(char) + 32)  # Convert uppercase to lowercase
    # If it's lowercase, change it to uppercase
    elif 'a' <= char <= 'z':
        swapped_text += chr(ord(char) - 32)  # Convert lowercase to uppercase
    # If it’s not a letter, just keep it the same
    else:
        swapped_text += char

# Print the final swapped string
print(swapped_text)
