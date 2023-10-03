class Employee:
    def __init__(self,name,salary,):
        self.name=name
        self.salary=salary
    def get_net_salary(self,allowance):
        net=self.salary*allowance/100
        return net
class Developer(Employee):
    def __init__(self,name,salary,app):
        self.app=app
        super().__init__(name,salary)
    def get_net_salary(self, allowance):
        a= super().get_net_salary(allowance)
        b= self.salary*self.app/100
        return a+b
e1=Developer("manoj",1000,20)
print(vars(e1))
print(e1.get_net_salary(20))








"""
class Employee:
    def __init__(self,employee_name,salary):
        self.employee_name=employee_name
        self.salary=salary
    def get_net_salary(self,allonces):
        alone= self.salary *allonces/100
        return self.salary +alone
class Developer(Employee):
    def __init__(self,employee_name,salary,application):
        super().__init__(employee_name,salary)
        self.application=application
    def get_net_salary(self,allonces):
        all=super().get_net_salary(allonces)
        app=self.salary*self.application/100
        return all+app
d1=Developer("manoj",1000,5)
print(vars(d1))
print(d1.get_net_salary(10))


"""