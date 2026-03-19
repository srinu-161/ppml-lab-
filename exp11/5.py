import numpy as np
arr = np.array([1, 2, 3, 4])
np.save('my_array.npy', arr)
load_arr = np.load('my_array.npy')

print(f"Loaded array : \n {load_arr}")