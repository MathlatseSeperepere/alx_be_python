# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while) to control rows
while row < size:
    # Inner loop (for) to control columns in each row
    for col in range(size):
        print("*", end="")  # Print * without moving to a new line
    print()  # Move to the next line after each row
    row += 1
