# Input marks
a = int(input("Enter your maths mark: "))
b = int(input("Enter your science mark: "))
c = int(input("Enter your english mark: "))
d = int(input("Enter your history mark: "))
e = int(input("Enter your geography mark: "))


total = a + b + c + d + e
percentage = (total / 250) * 100
def ast(a, b, c, d, e):
    return ((a + b + c + d + e) / 250) * 100

grade = (lambda p: 
         'O' if p >= 90 else 
         'E' if p >= 80 else 
         'A' if p >= 70 else 
         'B' if p >= 60 else 
         'C' if p >= 50 else 
         'F')(percentage)

print("Percentage:", percentage)
print("Grade:", grade)