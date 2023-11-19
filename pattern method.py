# pattern method for_loop
# pattern using numbers
# def number_pattern(rows):
n = int(input("enter a number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# number_pattern(10)

# pattern using alphabet
# def alphabet_pattern(rows):
n = int(input("enter a number:"))
start_char = ord('A')  # ASCII code for 'A'
for i in range(1, n+1):
    for j in range(1, i + 1):
        print(chr(start_char + j), end=" ")
    print()
# alphabet_pattern(26)

# half pyramid
# def half_pyramid(rows):
n = int(input("enter a number"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# Example: Print a half pyramid with 5 rows
# half_pyramid(5)

# fully pyramid chatgpt
def full_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces before the asterisks
        for j in range(rows - i):
            print(" ", end=" ")

        # Print the left side of the pyramid
        for k in range(1, i + 1):
            print("*", end=" ")

        # Print the right side of the pyramid
        for l in range(i - 1, 0, -1):
            print("*", end=" ")
    print()
# Example: Print a full pyramid with 5 rows
full_pyramid(5)

# right pyramid
def right_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces before the asterisks
        for j in range(rows - i):
            print(" ", end=" ")
        # Print the asterisks
        for k in range(1, i + 1):
            print("*", end=" ")
    print()
# Example: Print a right-angled pyramid with 5 rows
right_pyramid(5)
