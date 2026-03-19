arr=[]
x=int(input("enter the number of elements: \n "))
for i in range (x):
    m=int(input("enter the element : "))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("teh sorted array is :\n")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print(f"second largest element {second_largest}")
print(f"second samllest element {second_smallest}")