# This is a simple calculator program.

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def exponentiate(x, y):
   return x ** y

#Task 1 already in file
#Task 2:
def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")

    choice = input("Select operation (1/2/3/4/5): ")

    if choice not in ('1', '2', '3', '4', '5'):
        print("Invalid input. Please select a valid operation.")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()


# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.
# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.

