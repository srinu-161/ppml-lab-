#GCD of three numbers
import math

def gcd_three(a, b, c):
    return math.gcd(math.gcd(a, b), c)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("GCD of the three numbers is:", gcd_three(num1, num2, num3))