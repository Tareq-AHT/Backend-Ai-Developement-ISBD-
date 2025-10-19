# Assignment_3b. make a function that will take two numbers and 
# print the result of their sum, subtraction, multiplication and division

num1 = float(input("Insert the first number: "))
num2 = float(input("Insert the second number: "))


def operation_calculation (num1, num2):
    print("The summation is: ", num1 + num2)
    print("The substraction is: ", num1 - num2)
    print("The multiplication is: ", num1 * num2)
    
    if num2 != 0:
        print("The dividation is: ", num1 / num2)
    
    else:
        print("Dividation can not be possible by zero")
    
    

operation_calculation(num1, num2)
    