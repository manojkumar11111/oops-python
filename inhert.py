class Employee:
    def __init__(self,employee_name,email):
        self.employee_name=employee_name
        self.email=email
class Developer(Employee):
    def __init__(self,employee_name,email,skills):
        self.skills=skills
        super().__init__(employee_name,email)
class Manager(Employee):
    def __init__(self,employee_name,email,departments):
        self.departments=departments
        super().__init__(employee_name,email)
e1=Employee("manoj","manoj@2003")
print((e1))
d1=Developer("half","half@123",["analyst","designer"])
print(vars(d1))
m1=Manager("part","part@123",["dep1","dep2"])
print(vars(m1))