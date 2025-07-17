# Fun Calculator - Basic Arithmetic Operations 🧮✨

This Python script provides a simple and fun calculator that performs basic arithmetic operations on two numbers. It's designed with user-friendliness in mind and includes helpful error handling for division by zero.

## Features 🌟

- **Addition**: Sum of two numbers
- **Subtraction**: Difference between two numbers
- **Multiplication**: Product of two numbers
- **Division**: Quotient of two numbers (with zero division protection)
- **Decimal Support**: Handles both integers and decimals
- **User-Friendly**: Clear prompts and formatted output
- **Error Handling**: Gracefully handles division by zero

## How to Run 🚀

1. Ensure you have Python installed (Python 3.6 or newer recommended)
2. Save the code as `fun_calculator.py`
3. Run using:
   ```bash
   python fun_calculator.py
   ```
4. Follow the prompts to enter two numbers

## Example Usage 💻

```plaintext
Enter the first number: 12.5
Enter the second number: 4

Results of your two numbers:
sum: 16.5
difference: 8.5
product: 50.0
quotient: 3.125
```

## Division by Zero Handling ⚠️

If you attempt to divide by zero, the calculator will display:
```plaintext
quotient: undefined (can't divide by zero!)
```

## Code Structure 📝

```python
# 🎉 Welcome to the Fun Calculator! �
# Get first number input (supports decimals)
num1 = float(input("Enter the first number: "))

# Get second number input
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Handle division with zero check
quotient_result = num1 / num2 if num2 != 0 else "undefined (can't divide by zero!)"

# Display results
print("Results of your two numbers:")
print("sum:", sum_result)
print("difference:", difference_result)
print("product:", product_result)
print("quotient:", quotient_result)
```

## Requirements 🔧

- Python 3.x
- No external dependencies

Enjoy calculating with style! 😎✨
