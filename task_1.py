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
        return "Cannot divide by zero"

def expo(x, y):
   return x ** y

# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.
# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid input. Please enter a number between 1 and 5.")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        operation = 'addition'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = 'subtraction'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = 'multiplication'
    elif choice == '4':
        result = divide(num1, num2)
        operation = 'division'
    elif choice == '5':
        result = expo(num1, num2)
        operation = 'exponentiation'

    print(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    calculator()