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

def exponentiate(x,y):
    return x**y

keep_running = True

def read_code():
    s = input("What operation do you want to do (+,-,*,/,^):")
    
    if s=='exit':
        global keep_running
        keep_running = False
        return 'Closing'
    
    x = input("First number:")
    y = input("Second number:")
    print('You entered: '+x+s+y)
    x=float(x)
    y=float(y)
    if s=='+':
        return add(x, y)
    elif s=='-':
        return subtract(x, y)
    elif s=='*':
        return multiply(x, y)
    elif s=='/':
        return divide(x, y)
    elif s=='^':
        return exponentiate(x, y)
    else:
        raise ValueError('Unknown operation')
    
while keep_running:
    print(read_code())

# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.
# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.
# Task 3: Add a new file to the repo with other code of your choice

