# Get a string and a character/substring to find
text = input("Enter a string: ")
target = input("Enter the character or substring to find: ")

# Initialize index as None (indicating not found)
index = None

# Iterate through the string in reverse to find the last occurrence
for i in range(len(text) - len(target), -1, -1):  # Corrected range
    if text[i:i + len(target)] == target:
        index = i
        break  # Stop at the first (last-found) occurrence

# Print the result
if index is not None:
    print(f'The last occurrence of "{target}" is at index {index}.')
else:
    print(f'"{target}" not found in the string.')