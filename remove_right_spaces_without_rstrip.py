# Get a string from the user 
text = input("String: ")

# Initialize an index to the last character position
index = len(text) - 1

# Go through the string backwards and find the first non-space character
while index >= 0 and text[index] == ' ':
    index -= 1

# Return the part of the string up to that position (inclusive)
print(text[:index + 1])