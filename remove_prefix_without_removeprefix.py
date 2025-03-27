# Get input from the user
text = input("String: ")
prefix = input("Prefix to remove: ")

# If the string starts with the prefix
if text[:len(prefix)] == prefix:
    # Remove the prefix by slicing the string
    text = text[len(prefix):]

# Print the result 
print(text)
