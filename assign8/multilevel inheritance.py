class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"hi i am {self.name} and im {self.age}")
class employee(person):
    def __init__(self,name,age,emp_id,designation):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.designation=designation
    def employee_details (self):
        print(f"employe id : {self.emp_id} designation:  {self.designation}")
class manager(employee):
    def __init__(self,name,age,emp_id,designation,team_size):
        super().__init__(name,age,emp_id,designation,)
        self.team_size=team_size
    def manager_details(self):
        print(f"manager's team size : {self.team_size}")
manager1=manager("sugu","23",1234,"data analyst",12)
manager1.introduce()
manager1.employee_details()
manager1.manager_details()