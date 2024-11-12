def string (str):
    if not str:
         raise  ValueError("ath patoola")
    else:
         print(f"string:{str}")
try:
     user=input("enter a string:")
     string(user)
except ValueError as e:
    print({e})