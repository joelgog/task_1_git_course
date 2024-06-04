# This is a simple calculator program.

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y != 0:  # Check for division by zero
        	return x / y
	else:
        	return "Cannot divide by zero."

def exponentiate(x, y):
	return x ** y

def read():
	op = input("Enter operation:")
	x = float(input("Enter first number:"))
	y = float(input("Enter second number:"))


	if op == "add":
		return add(x, y)
	elif op == "subtract":
		return subtract(x, y)
	elif op == "multiply":
		return multiply(x, y)
	elif op == "divide":
		return divide(x, y)
	elif op == "exponentiate":
		return exponentiate(x, y)

while True:
	print(read())

# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.
# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.
# Task 3: Add a new file to the repo with other code of your choice

