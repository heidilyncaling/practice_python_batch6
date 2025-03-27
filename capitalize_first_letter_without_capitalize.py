# Get a string
text = input("Enter a string: ")

# Make the first letter uppercase
first_letter = text[0]
if 'a' <= first_letter <= 'z':
    first_letter = chr(ord(first_letter) - 32)

# Make all other letters lowercase
rest_of_text = ""
for char in text[1:]:
    if 'A' <= char <= 'Z': 
        rest_of_text += chr(ord(char) + 32)
    else:
        rest_of_text += char

# Combine the first letter with the rest
text = first_letter + rest_of_text

print(text)
