m=int(input("enter the starting number : "))
n=int(input("enter the last number : "))
lis=[] 
c=0
for i in range (m,n+1):
    for j in range (2,i):
        if i%j==0:
            break
        else:
            lis.append(i)
print("your prime number list is : ",list(set(lis)))
    
