class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce1(self):
        print(f"hi i am {self.name} and i am {self.age} years old")
class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def introduce(self):
        super().introduce1()
        print(f"Hi, I am {self.name} and I am {self.age} years old, and I am in grade {self.grade}.")
student1=student("aysha",21,12)
student1.introduce()
