class debit_trans:
    def __init__(self,debit_number,debit_amount,*args):
        print("enter debit class")
        self.debit_number=debit_number
        self.debit_amount=debit_amount
        super(debit_trans,self).__init__(*args)
        print("exit debit class")

class credit_trans:
    def __init__(self,credit_number,credit_amount,*args):
        print("enter credit class")
        self.credit_number=credit_number
        self.credit_amount=credit_amount
        super(credit_trans,self).__init__(*args)
        print("exit credit class")


class fund_trans(debit_trans,credit_trans):
    def __init__(self,debit_number,debit_amount,credit_number,credit_amount,trans_amount):
        print("enter fund class")
        self.trans_amount=trans_amount
        super(fund_trans,self).__init__(debit_number,debit_amount,credit_number,credit_amount)
        print("exit funds class")
print(fund_trans.mro())
f1=fund_trans(102,1000,201,1000,"19-10-2023")
print(vars(f1))
