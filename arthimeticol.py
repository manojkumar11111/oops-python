class Trans:
    def __init__(self,trans_amount,trans_date):
        self.trans_amount=trans_amount
        self.trans_date=trans_date
    def __mul__(self,other):
        return Trans(self.trans_amount*other.trans_amount,max(self.trans_date,other.trans_date))
t1=Trans(10,"22-10")
t2=Trans(20,"19-10")
t3=Trans(30,"10-19")
print(vars(t1*t2*t3))

class tra:
    def __init__(self,trans_amount,trans_date):
        self.trans_amount=trans_amount
        self.trans_date=trans_date
    def __div__(self,other):
        return self.trans_amount/other.trans_amount
    
t1=tra(10,"10-20")
t2=tra(20,"20-01")
print(t1/t2)