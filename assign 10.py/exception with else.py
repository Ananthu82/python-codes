def number():
    try:
        num=int(input("enter a number:"))
    except ValueError:
        print("enter a valid number")
    else:
        print(f"the number entered is : {num}")
number()