# Get a string and a character/substring to find
text = input("Enter a string: ")
target = input("Enter the character or substring to find: ")

# Initialize index to -1 (indicating not found)
index = -1

# Iterate through the string to find the first occurrence
for i in range(len(text) - len(target) + 1):
    if text[i:i+len(target)] == target:
        index = i
        break  # Stop at the first occurrence

# Print the result
if index != -1:
    print(f'The first occurrence of "{target}" is at index {index}.')
else:
    print(f'"{target}" not found in the string.')