# wap to create a list containing natural numberfrom m  to n where m and n given input.
m=int(input("enter the starting number : "))
n=int(input("enter the last number : "))
lis=[]
for i in range (m,n+1):
    lis.append(i)
print("your desired list is : ")
print(lis)
print("smallest element in the list : ",m)
print("largest element in the list :",n)
print ("sum of all elements in list :",sum(lis))
print("average of all elements of the list :",sum(lis)/(n-m+1))


    