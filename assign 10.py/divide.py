def divide():
    try:
        num1=int(input("enter first number: "))
        num2=int(input("enter second number: "))
        result=num1/num2
    except ZeroDivisionError:
        print("division by zero is invalid")
    else:
        print(f"result after division:{result}")
divide()