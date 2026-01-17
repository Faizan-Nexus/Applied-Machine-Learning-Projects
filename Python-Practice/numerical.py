import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [1,2,3,4,5]])
print(arr.shape)
arr_2 = arr[0].reshape(5, 1)

print(arr_2)