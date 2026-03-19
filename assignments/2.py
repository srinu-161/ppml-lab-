x=int(input("enter a number :\n"))
fact=1
if x<0:
    print("it is a negative number ")
elif x==0:
    print(f"The factorial of {x} is {fact}")
else:
    for i in range (1,x+1):
        fact=fact*i
    print(f"The factorial of {x} is {fact}")