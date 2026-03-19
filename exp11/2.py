import numpy as np
arr= np.array(
    [1,2,3],
    dtype='int32')
print (f"\n---------------------------------------\nData type : {arr.dtype}\n----------------------------------------\n")
arr=arr.astype(np.float64)
print (f"Updated Data type {arr.dtype}\n----------------------------------------\n")
