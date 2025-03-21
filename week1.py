#A simple Python program that asks the user to input two numbers 
# and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.

#Use the input() function to receive user input.
num1 = int(input("Enter the first number: "))
operation = input("Enter the operation you want to perform(+, *, /, -): ")
num2 = int(input("Enter the second number: "))
#Use if statements to determine which operation to perform.
if operation == "+" :
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")   
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")   
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}") 
elif operation == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}") 
else:
    print("Invalid operation. Please enter +, -, /, *")

