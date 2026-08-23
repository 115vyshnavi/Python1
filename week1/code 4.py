num1 = int(input("Enter 1st Num: "))
num2 = int(input("Enter 2nd Num: "))
operator = input("Enter Operator: ")
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Enter a valid operator"
result = calculator(num1, num2, operator)
print("Result:", result)