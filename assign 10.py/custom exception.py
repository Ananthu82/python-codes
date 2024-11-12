class NegativeNumberError (Exception) :
     pass
def check_positive (number) :
     if number <0:
       raise NegativeNumberError("Error: Negative numbers are not allowed.")
     print(f"Number entered: {num}")
try:
    num = int(input("Enter a number: "))
    check_positive(num)

except NegativeNumberError as e:
    print (e)
NegativeNumberError()