class employee:
    def __init__(self,empid,name,basic_pay):
        self.empid=empid
        self.name=name
        self.basic_pay=basic_pay
        
    def calc(self):
        
        T=0.1*self.basic_pay
        D=0.4*self.basic_pay
        calculated=self.basic_pay+T+D
        return f"{calculated}"
    def disp(self):
        return f"""\nEmployee name is {self.name}\nEmployee ID is {self.empid}\nEmployee Basic_Pay : {self.basic_pay}\nEmployee's Gross_pay : {self.calc()} \n"""

  
emp1=employee(110,"Ramesh",30000)
emp2=employee(112,"Ram",80000)              
print(f"Employee Detail's : \n {emp1.disp()}")
print(f"Employee Detail's : \n {emp2.disp()} \n ")