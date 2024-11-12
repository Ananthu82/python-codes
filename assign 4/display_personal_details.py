def display_personal_details(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}:{values}")
display_personal_details(name="sharan",age=23,email="abc123@gmail.com")
