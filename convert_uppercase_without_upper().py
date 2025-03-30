# Get a string from the user
text = input("String: ")

result = ''

# Iterate over each character in the original string
for char in text:
    # Check if the character is a lowercase letter
    if 'a' <= char <= 'z':
        # Convert to uppercase using ASCII values
        result += chr(ord(char) - 32)
    else:
        # If not a lowercase letter
        result += char

# Print the result
print(result)