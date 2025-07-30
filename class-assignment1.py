#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# and then performs the operation on the two numbers.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    result = "Invalid operation"

print("The result is:", result)