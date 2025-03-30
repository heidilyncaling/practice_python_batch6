# Get a string from the user
text = input("String: ")

# Assume it's all lowercase
all_lower = True  

# Go through each letter
for char in text:
    # If you find even one uppercase letter, return False immediately
    if 'A' <= char <= 'Z':
        all_lower = False
        break

# Print the result
print(all_lower)