import numpy as np

arr = np.random.randint(0,1000, size=(5,5), dtype=int)
print(arr)
print(arr[1,2])
print(np.sum(arr))
print(np.mean(arr, axis=1))
print(np.max(arr, axis=0))