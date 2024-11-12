try:
    f=open(r"text.txt")
    try:
        content=f.read()
        print(content)
        num1=input("enter number:")
        num2=input("enter a number:")
        result=num1/num2
    except ZeroDivisionError:
        print("cannot divisible by zero")
    finally:
        f.close()
except FileNotFoundError:
    print("the given file is not found")
    


    