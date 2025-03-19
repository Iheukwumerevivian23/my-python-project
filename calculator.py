# create a function for multiplication
def multiply(num1, num2):
    return num1 * num2
# Create a function to divide
def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return num1 / num2
# Create a function to add
def addition(num1, num2):
    return num1 + num2
# Create a function to substract
def subtract(num1, num2):
    return num1 - num2

def calculator():
    result = None
    while True:
        print("Welcome to my calculator")
        print("Please choose an operation:")
        print("1. Addition", "\n2. Multiplication", "\n3. Division", "\n4. Subtraction")
        choice = input("Please choose an operation (1-4): ")
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please choose a valid option.")
            continue
        
        if result is None:
            num1 = int(input("First Number: "))
            num2 = int(input("Second Number: "))
        else:
            use_prev = input(f"Do you want to use the previous result ({result})? (first/second/no): ").strip().lower()
            
            if use_prev == "first":
                num1 = result
                num2 = int(input("Second Number: "))
            elif use_prev == "second":
                num1 = int(input("First Number: "))
                num2 = result
            else:
                num1 = int(input("First Number: "))
                num2 = int(input("Second Number: "))
        
        if choice == "1":
            result = addition(num1, num2)
        elif choice == "2":
            result = multiply(num1, num2)
        elif choice == "3":
            result = divide(num1, num2)
        elif choice == "4":
            result = subtract(num1, num2)
        
        if result is not None:
            print("Result:", result)
        
        again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Calculator exiting. Goodbye!")
            break

calculator()
