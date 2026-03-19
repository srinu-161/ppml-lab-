class Addition:
    def add(self, a, b):
        return a + b


class Subtraction:
    def subtract(self, a, b):
        return a - b


class Multiplication:
    def multiply(self, a, b):
        return a * b


class Division:
    def divide(self, a, b):
        if b == 0:
            return "Division by zero not allowed"
        return a / b

class Calculator(Addition, Subtraction, Multiplication, Division):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def perform_operations(self):
        print(f"Addition: {self.add(self.data1, self.data2)}")
        print(f"Subtraction: {self.subtract(self.data1, self.data2)}")
        print(f"Multiplication: {self.multiply(self.data1, self.data2)}")
        print(f"Division: {self.divide(self.data1, self.data2)}")
print("Enter the to numbers : ")
a=int(input("Number 1 : "))
b=int(input("\nNumber 2 : "))

calc = Calculator(a,b)
calc.perform_operations()