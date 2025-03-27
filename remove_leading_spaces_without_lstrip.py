# Get a string from the user 
text = input("String: ")

# Go through each character. Stop in first non-space character  
index = 0
while index < len(text) and text[index] == ' ':
    index += 1

# Return the part of the string starting from that position  
print("Result:", text[index:])
