#find greatest among 3 integer and equal number
x=int(input("enter a integer"))
y=int(input("enter a integer"))
z=int(input("enter a integer"))
greatest = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

if x == y == z:
    print("All numbers are equal:", x)
else:
    print("The greatest number is:", greatest(x, y, z))
