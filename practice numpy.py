import numpy as np

array = np.array([1,2,3,4,5,6])
print(array)

print("shape", array.shape)

print("Size:", array.size)

print("Data Type:", array.dtype)

# Accessing elements
print("First element:", array[0])            # First element
print("Last element:", array[-1])            # Last element
print("Elements from index 1 to 4:", array[1:5])  # Slicing

array[0] = 10
print("Modified Array:", array)

print(array)
zeros_array = np.zeros((3, 4))  # 3x4 array of zeros
print("Zeros Array:\n", zeros_array)

# empty_array = np.empty((2, 2))  # 2x2 empty array (uninitialized)
# print("Empty Array:\n", empty_array)

arange_array = np.arange(0, 10, 2)  # Array from 0 to 10 with step 2
print("Arange Array:", arange_array)

linspace_array = np.linspace(0, 100, 5)  # 5 points from 0 to 1
print("Linspace Array:", linspace_array)

# Addition
print("Array + 2:", array + 2)

# Element-wise multiplication
print("Array * 2:", array * 2)

# Square root
print("Square Root:", np.sqrt(array))

# Sum
print("Sum of Elements:", np.sum(array))

# Mean
print("Mean:", np.mean(array))

reshaped_array = array.reshape((3, 2))  # Reshape to 2x3
print("Reshaped Array:\n", reshaped_array)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Vertical Stack
vstacked = np.vstack((array1, array2))
print("Vertical Stack:\n", vstacked)

# Horizontal Stack
hstacked = np.hstack((array1, array2))
print("Horizontal Stack:", hstacked)

filtered_array = array[array > 2]  # Elements greater than 3
print("Filtered Array (greater than 3):", filtered_array)

print("Max:", np.max(array))
print("Min:", np.min(array))
print("Standard Deviation:", np.std(array))

# insert value
Array = np.array ([0,2,3,4,5,6])
Array = np.insert(Array,1,1)
print(Array)







