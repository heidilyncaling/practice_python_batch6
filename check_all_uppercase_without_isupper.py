# Get a string from the user
text = input("String: ")

# Assume it's all uppercase
all_upper = True  

# Go through each letter
for char in text:
    # If you find even one lowercase letter, return False immediately
    if 'a' <= char <= 'z':
        all_upper = False
        break

# Print the result
print(all_upper)
