def calculate_sum(a,b):
    print(a+b)
calculate_sum(1,2)
# with arguments and with return type
def calculate_sum(a, b):
    result = a + b
    return result
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = calculate_sum(num1, num2)
print(f"The sum of {num1} and {num2} is: {sum_result}")

