# Get a string
text = input("String:")

# Split the string into words
words = text.split()

# Process each word
title_cased_words = []
for word in words:
    # Make the first letter uppercase
    first_letter = word[0]
    if 'a' <= first_letter <= 'z':  # Convert to uppercase if it's lowercase
        first_letter = chr(ord(first_letter) - 32)

    # Make the rest of the letters lowercase
    rest_of_word = ""
    for char in word[1:]:
        if 'A' <= char <= 'Z':  # Convert to lowercase if it's uppercase
            rest_of_word += chr(ord(char) + 32)
        else:
            rest_of_word += char

    # Combine and add to the list
    title_cased_words.append(first_letter + rest_of_word)

# Join words back into a string
result = " ".join(title_cased_words)

# Print the final result
print(result)
