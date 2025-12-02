class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def ShowDetails(self):
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","Software",1000000)

E=Engineer("Sinchana",19)
E.ShowDetails()
