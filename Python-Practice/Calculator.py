check = ["*", "+", "/", "-", "%"]

while True:
    oper = input("Enter the operations (+,-,*,/,%): ")
    if oper not in check:
        print(f"{oper} is not a valid operator! Try again")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if oper == "+":
        result = num1 + num2
    elif oper == "-":
        result = num1 - num2
    elif oper == "*":
        result = num1 * num2
    elif oper == "/":
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        result = num1 / num2
    elif oper == "%":
        if num2 == 0:
            print("Error: Modulo by zero!")
            continue
        result = num1 % num2

    print(f"{num1} {oper} {num2} = {round(result,3)}")
    break