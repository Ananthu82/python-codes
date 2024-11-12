def division():
    try:
        numerator=int(input("enter a number"))
        denominator=int(input("enter a number"))
        if denominator==0:
            raise ZeroDivisionError("integer cannod be divided by zero")
        result=numerator/denominator
        print(f"result after division:{result}")
    except ZeroDivisionError as e:
        print({e})
division()

