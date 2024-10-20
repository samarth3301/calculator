# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to raise a number to a power
def power(x, y):
    return x ** y

# Function to divide two numbers
def divide(x, y):
    return x / y

print("Select an operation by selecting 1, 2, 3, 4, or 5:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Power")
print("5. Division")

while True:
    operation = input("Enter the operation number: ")
    
    if operation in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
        
        if operation == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == "4":
            print(f"{num1} ** {num2} = {power(num1, num2)}")
        elif operation == "5":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        continue_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_calc == "no":
            break
    else:
        print("Invalid input! Please select a number between 1 and 5.")
