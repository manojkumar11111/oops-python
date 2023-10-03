class employee:
    def __init__(self,e_name,salary):
        self.e_name=e_name
        self.salary=salary
    def net_det(self,net_amount):
        amount=self.salary-net_amount
        print(amount) 
class developer(employee):
    def __init__(self,e_name,salary,mon_amount):
        super().__init__(e_name,salary)
        self.mon_amount=mon_amount

    def net_det(self,net_amount):
        part1=super().net_det(net_amount)
        part2=self.mon_amountt
        return part1 + part2

e1=developer("manoj",2500,500)
print(vars(e1))
e=employee("manu",3000)
print(vars(e))
e.net_det(500)
print(e1.net_det(50))