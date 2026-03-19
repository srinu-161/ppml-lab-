#wap to input 3 coefficient values and find real roots
import math
a=int(input ("enter coefficien of x2 : "))
b=int(input("enter coefficient of x : "))
c=int(input("enter constant : "))
if ((b**2)-(4*a*c))<0:
    print ("no real roots")
else:
   d=math.sqrt((b**2)-(4*a*c))

   x1=(-b+d)/(2*a)
   x2=(-b-d)/(2*a)
   print("first root is : ",x1)
   print ("second root is : ",x2)