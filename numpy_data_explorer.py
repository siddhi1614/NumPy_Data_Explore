import numpy as np
import time

print("Enter 5 number of array 1 : ")
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.arange(1, 10)

print("Array:", arr1)
print("Slice:", arr1[1:4])

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
print("Addition:", a + b)

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print("Mean:", np.mean(data))
print("Sum Axis 0:", np.sum(data, axis=0))

reshaped = arr2.reshape(3, 3)
print("Reshaped:\n", reshaped)


np.save("saved_array.npy", reshaped)
print("Loaded:\n", np.load("saved_array.npy"))


size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size)

start = time.time()
python_list = [x * 2 for x in python_list]
print("Python list time:", time.time() - start)

start = time.time()
numpy_array = numpy_array * 2
print("NumPy time:", time.time() - start)
