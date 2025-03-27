# Get string and an ending part
text = input("String: ")
ending = input("Ending part to check: ")

# Find out how long the ending part is
end_length = len(ending)

# Grab the last part of the string with the same length
last_part = text[-end_length:]

# Compare it to the given ending part
result = last_part == ending

# Print the result
print(result)
