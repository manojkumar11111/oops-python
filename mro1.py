class debit:
    def __init__(self,d_account,d_amount,*args):
        print("hii")
        self.d_account=d_account
        self.d_amount=d_amount
        super(debit,self).__init__(*args)
        print("hii2")
class credit:
    def __init__(self,c_account,c_amount,*args):
        print("hii1")
        self.c_account=c_account
        self.c_amount=c_amount
        super(credit,self).__init__(*args)
        print("hii1")
class transfer(debit,credit):
  def __init__(self,d_account,d_amount,c_account,c_amount,trans_amount):
        print("hii2")
        self.trans_time=trans_amount
        super(transfer,self).__init__(d_account,d_amount,c_account,c_amount)
        print("hii")

print(transfer.mro())
e1=transfer(101,2000,201,2000,19-10-2023)
print(vars(e1))

