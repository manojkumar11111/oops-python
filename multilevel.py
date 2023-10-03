class Transiction:
    def __init__(self,transaction_description,transaction_amount):
        self.transaction_description=transaction_description
        self.transaction_amount=transaction_amount
class Debit_Transiction(Transiction):
    def __init__(self,debit_account_number,transaction_description,transaction_amount):
        self.debit_account_number=debit_account_number
        super().__init__(transaction_description,transaction_amount)
class Bill_payment(Debit_Transiction):
    def __init__(self,bill_name,debit_account_number,transaction_description,transaction_amount):
        self.bill_name=bill_name
        super().__init__(debit_account_number,transaction_description,transaction_amount)
e1=Bill_payment("savings",12345678965,"for heath",10000)
print(vars(e1))