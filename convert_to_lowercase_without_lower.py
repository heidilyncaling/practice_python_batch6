# Get a string from the user
text = input("String: ")

# empty string to store the result
result = ""

# Go through each character in the string
for char in text:
    # If it’s an uppercase letter (A-Z), turn it into lowercase by adding 32
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)  # Convert uppercase to lowercase
    else:
        result += char  # Keep everything same

# Finally, print the new string where everything is in lowercase
print(result)
