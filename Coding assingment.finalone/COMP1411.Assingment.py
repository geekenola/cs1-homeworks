import math

# Function to display the welcome message and menu options
def welcome():
    print("Welcome to the Interactive Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication ")
    print("4. Division")
    print("5. Square Root")
    print("6. Quit")

# Function to Addition
def Add(x, y):
    print(f"Result: {x} + {y} = {x + y}")

# Function to Subtraction
def Sub(x, y):
    print(f" Result: {x} - {y} = {x - y}")

# Function to Multiplication
def Multi(x, y):
    print(f"Result: {x} * {y} = {x * y}")

# Function to Division
def Div(x, y):
    while y == 0:
        y = float(input("Number cannot be divided by zero. Enter your number again: "))
    print(f"Result: {x} / {y} = {x / y}")

# Function to calculate square root
def root(x):
    while x < 0:
        x = float(input("We cannot take the square root of a negative number. Enter your number again: "))
    else:
        print(f" Result: Square root  of {x} = {math.sqrt(x)}")

# Main program (while loop)
while True:
    welcome()
    select_option = int(input("Enter your choice (1/2/3/4/5/6): "))
    if select_option == 1:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        Add(x, y)
    elif select_option == 2:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        Sub(x, y)
    elif select_option == 3:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        Multi(x, y)
    elif select_option == 4:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        Div(x, y)
    elif select_option == 5:
        x = float(input("Enter a positive number: "))
        root(x)
    elif select_option == 6:
        print("Goodbye!")
        break  # Exit the loop when option 6 is selected
    else:
        print("Invalid option. Please select a valid option (1-6)")
