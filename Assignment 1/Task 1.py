# Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

# Check before division to avoid division by zero
if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Division: Cannot divide by zero")

