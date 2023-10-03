class Debit_account:
    def __init__(self,debit_number,debit_amount):
        self.debit_number=debit_number
        self.debit_amount=debit_amount
    
class Credit_account:
    def __init__(self,credit_number,credit_amount):
        self.credit_number=credit_number
        self.credit_amount=credit_amount
    
class transfer(Debit_account,Credit_account):
    def __init__(self,debit_number,debit_amount,credit_number,credit_amount,transfer_date):
        
        Debit_account.__init__(self,debit_number,debit_amount)
        Credit_account.__init__(self,credit_number,credit_amount)
        self.transfer_date=transfer_date
e1=transfer(123,1000,321,1000,"19-10--2023")
print(vars(e1))
