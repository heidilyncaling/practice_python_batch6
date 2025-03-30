# Get string and a starting part
text = input("String: ")
starting = input("Starting part to check: ")

# Find out how long the starting part is
start_length = len(starting)

# Grab the first part of the string with the same length
first_part = text[:start_length]

# Compare it to the given starting part
result = first_part == starting

# Print the result
print(result)
