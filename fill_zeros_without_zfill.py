# Get a string and a target length
text = input("Enter a string: ")
target_length = int(input("Enter the target length: "))

# Check how long the string currently is
current_length = len(text)

# If it's shorter than the target, add zeros to the beginning
if current_length < target_length:
    # Figure out how many zeros are needed
    zeros_needed = target_length - current_length
    # Add those zeros to the beginning of the string
    text = '0' * zeros_needed + text

# Print the final result
print(f'"{text}"')