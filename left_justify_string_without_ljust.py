# Get a string and a target length
text = input("Enter a string: ")
target_length = int(input("Enter the target length: "))

# Check how long the string currently is
current_length = len(text)

# If it's shorter than the target, add spaces to the end
if current_length < target_length:
    # Figure out how many spaces are missing
    spaces_needed = target_length - current_length
    # Add those spaces to the end of the string
    text += ' ' * spaces_needed

# Print the final result (wrapped in quotes to show spaces)
print("Result:", f'"{text}"')
