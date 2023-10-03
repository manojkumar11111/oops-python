class student:
    def __init__(self,stu_name,stu_number):
        self.name=stu_name
        self.number=stu_number
    def getdetailes(self):
         print( f"hi my name is {self.name},my id is {self.number}.")
class teacher(student):
     def __init__(self,teacher_name,teacher_id,salary):
            
            super().__init__(teacher_name,teacher_id)
            self.nam=salary
e=student("manoj",520)
print(vars(e))
e.getdetailes()
e1=teacher("manu",515,2000.0)
print(vars(e1))
e1.getdetailes()