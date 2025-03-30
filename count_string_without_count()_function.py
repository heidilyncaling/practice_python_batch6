# Get a string and a character/substring to count
text = input("Enter a string: ")
target = input("Enter the character or substring to count: ")

# Initialize a counter
count = 0

# Iterate through the string and check
for i in range(len(text) - len(target) + 1):
    if text[i:i+len(target)] == target:
        count += 1

# Print the final count
print(f'"{target}" appears {count} times in the string.')