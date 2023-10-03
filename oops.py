#from datetime import date
class Employee:
    def __init__(self,employee_name,age,job):
        self.employee_name=employee_name
        self.age=age
        self.job=job
    def birth(cls,employee_name,birth_year,job):
        age= date.today().year- birth_year
        return cls(employee_name,age,job)
e1=Employee("manoj",21,"developer")
e2=Employee("part",23,"analyst")
print(vars(e1))
print(vars(e2))
e3=Employee.birth("man",20,"designer")
print(vars(e3))
