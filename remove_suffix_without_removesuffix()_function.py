# Get a string from user
text = input("String: ")
suffix = input("Suffix to remove: ")

# Calculate the new length of the string without the suffix
new_length = len(text) - len(suffix)
# Get the substring without the suffix
result = text[:new_length]

# Print the result
print(result)