import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[10,20,30],[40,50,60]])
print(f"Array one : \n {arr}\n----------------------------\n")
print(f"Element at (0,1) of arr2 \n {arr2[0,1]} \n-----------------\n")
print(f"Row one : \n {arr[0,:]}\n\n")
print(f"column  one : \n {arr[:,0]}\n-------------------\n")