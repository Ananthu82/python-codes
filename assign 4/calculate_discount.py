def calculate_discount(price,discount=10):
    discount_amount=(discount/100)*price
    total= price - discount_amount
    return total

default_discount=calculate_discount(10)
print("total_price=",default_discount)

custom_discount=calculate_discount(10,20)
print("total_price=",custom_discount)