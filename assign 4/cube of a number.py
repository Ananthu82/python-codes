cube=lambda x:x**3
numbers=[1,3,4,5,6,7,8,9]
cube_of_numbers=list(map(cube,numbers))
print(f"cube of given numbers:{cube_of_numbers}")
filter_function=lambda y:y>100
greater_numbers=list(filter(filter_function,cube_of_numbers))
print(f"numbers greater than 100:{greater_numbers}")
