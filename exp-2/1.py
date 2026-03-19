p=float(input("Enter the principal"))
r=float(input("Enter the rate of intrest"))
t=float(input("Enter the time period"))
si=(p*r*t)/100
A=p*((1+r)/100)**t
ci=A-p
print("simple Intrest " , si)
print(f"Compound intrest : {ci}")