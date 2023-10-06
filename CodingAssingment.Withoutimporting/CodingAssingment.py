# Function to display the welcome message and menu options
def welcome():
    print("Welcome to the Interactive Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Quit")

# Function to Addition
def add(x, y):
    return x + y

# Function to Subtraction
def subtract(x, y):
    return x - y

# Function to Multiplication
def multiply(x, y):
    return x * y

# Function to Division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

# Function to calculate square root
def square_root(x):
    if x < 0:
        return "Cannot take the square root of a negative number."
    return x ** 0.5

# Main program (while loop)
while True:
    welcome()
    select_option = int(input("Enter your choice (1/2/3/4/5/6): "))
    if select_option == 1:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = add(x, y)
        print(f"Result: {x} + {y} = {result}")
    elif select_option == 2:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = subtract(x, y)
        print(f"Result: {x} - {y} = {result}")
    elif select_option == 3:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = multiply(x, y)
        print(f"Result: {x} * {y} = {result}")
    elif select_option == 4:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = divide(x, y)
        print(f"Result: {x} / {y} = {result}")
    elif select_option == 5:
        x = float(input("Enter a positive number: "))
        result = square_root(x)
        print(f"Result: Square root of {x} = {result}")
    elif select_option == 6:
        print("Goodbye!")
        break  # Exit the loop when option 6 is selected
    else:
        print("Invalid option. Please select a valid option (1-6)")
