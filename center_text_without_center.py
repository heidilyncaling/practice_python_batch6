# Get a string and a target length
text = input("String: ")
target_length = int(input("Target length: "))

# Find out how long the string currently is
current_length = len(text)

# If it’s shorter than the target, center it by adding spaces
if current_length < target_length:
    # Figure out how many spaces are needed
    total_spaces = target_length - current_length
    # Split them evenly for left and right sides
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    # Add spaces on both sides
    text = (' ' * left_spaces) + text + (' ' * right_spaces)

# Print the final result (wrapped in quotes to show spaces)
print(f'"{text}"')
