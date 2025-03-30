# Get a string and a target length
text = input("Enter a string: ")
target_length = int(input("Enter the target length: "))

# Check how long the string currently is
current_length = len(text)

# If it's shorter than the target, add spaces to the beginning
if current_length < target_length:
    # Figure out how many spaces are needed
    spaces_needed = target_length - current_length
    # Add those spaces to the beginning of the string
    text = ' ' * spaces_needed + text

# Print the final result
print(f'"{text}"')