# speed formula
def calculate_speed(distance, time):
    try:
        # Convert input to float to handle decimal values
        distance = float(distance)
        time = float(time)

        # Check if time is not zero to avoid division by zero
        if time != 0:
            speed = distance / time
            print(f"Speed: {speed} units per time")
        else:
            print("Time should be greater than zero to calculate speed.")
    except ValueError:
        print("Invalid input. Please enter numeric values for distance and time.")
# Get user input for distance and time
distance = input("Enter distance: ")
time = input("Enter time: ")
# Call the function to calculate and print speed
calculate_speed(distance, time)

# distance formula
import math

def calculate_distance(x1, y1, x2, y2):
    try:
        # Convert input to float to handle decimal values
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

        # Calculate distance using the formula
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"Distance: {distance} units")
    except ValueError:
        print("Invalid input. Please enter numeric values for coordinates.")
# Get user input for coordinates of two points
x1 = input("Enter x-coordinate of point 1: ")
y1 = input("Enter y-coordinate of point 1: ")
x2 = input("Enter x-coordinate of point 2: ")
y2 = input("Enter y-coordinate of point 2: ")
# Call the function to calculate and print distance
calculate_distance(x1, y1, x2, y2)

# car speed formula
def calculate_time(distance, speed):
    try:
        # Convert input to float to handle decimal values
        distance = float(distance)
        speed = float(speed)

        # Check if speed is not zero to avoid division by zero
        if speed != 0:
            time = distance / speed
            print(f"Time: {time} units")
        else:
            print("Speed should be greater than zero to calculate time.")
    except ValueError:
        print("Invalid input. Please enter numeric values for distance and speed.")
# Get user input for distance and speed
distance = input("Enter distance: ")
speed = input("Enter speed: ")
# Call the function to calculate and print time
calculate_time(distance, speed)

# average formula
def calculate_average(numbers):
    try:
        # Convert input to float to handle decimal values
        numbers = [float(num) for num in numbers]

        # Calculate the average
        average = sum(numbers) / len(numbers)
        print(f"Average: {average}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the list of numbers.")
# Get user input for a list of numbers
numbers_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = numbers_input.split()
# Call the function to calculate and print the average
calculate_average(numbers_list)

# light formula
def calculate_light_distance(time):
    try:
        # Speed of light in meters per second
        speed_of_light = 3.00e8

        # Convert time to float to handle decimal values
        time = float(time)

        # Calculate distance using the formula
        distance = speed_of_light * time
        print(f"Distance traveled by light: {distance} meters")
    except ValueError:
        print("Invalid input. Please enter a numeric value for time.")
# Get user input for time
time = input("Enter time (in seconds): ")
# Call the function to calculate and print the distance
calculate_light_distance(time)

# heat convert fahrenheit
celsius = 40
fahrenheit = (celsius*9/5)+32
print(fahrenheit)