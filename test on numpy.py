# Q.1 How do you create a NumPy array?

#You can create a NumPy array using the numpy library

import numpy as np

# From a list
arr = np.array([1, 2, 3, 4, 5])
print(arr) 

# Q.2 How do you create a 2D array (matrix) in NumPy?		

# we can create a 2D array (or matrix) in NumPy using this methods

matrix_from_lists = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix_from_lists)

#Q.3 How do you find the shape of an array?		

# we can find the shape of a NumPy array using the .shape method

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

shape = matrix.shape
print(shape)

# Q.4 How do you get the data type of a NumPy array?		

# we can get the data type of a NumPy array using the .dtype method

arr = np.array(['a', 'b', 'c'])
print(arr.dtype) 

# Q.5 How do you slice a NumPy array?		

# we can slice a numpy with these methods
array_1d = np.array([0, 1, 2, 3, 4, 5])

# Slice from index 1 to 4
slice_1d = array_1d[1:5]  
print(slice_1d)

# Slice with a step
step_slice_1d = array_1d[::2]  
print(step_slice_1d)


#  Q.6 How do you add or subtract two NumPy arrays?		

# we can add or subtract two NumPy arrays using the + and - operators, respectively

# Create two NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Add the arrays
result_add = array1 + array2 
print(result_add)

#  Subtract the arrays
result_subtract = array1 - array2  
print(result_subtract)

# Q.7 How do you transpose a 2D NumPy array?		

# we can transpose a 2D NumPy array using the .T or the numpy.transpose() function

# Create a 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

# Transpose the array
transposed_array = array_2d.T
print(transposed_array)	

# Q.8 How do you perform element-wise multiplication in NumPy?	

# we can perform element-wise multiplication in NumPy using the * operator

# Create two NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise multiplication
result = array1 * array2  # Output: array([ 4, 10, 18])
print(result)

# Q.9 How do you calculate the sum of elements in a NumPy array?			

# we can calculate the sum of elements in a NumPy array using 
# the numpy.sum() function or the .sum() method

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Calculate the sum
total_sum = np.sum(array)
print(total_sum) 

# Q.10 How do you create an array of evenly spaced values?			

# You can create an array of evenly spaced values in NumPy using the numpy.arange() and numpy.linspace()


# Create an array of evenly spaced values from 0 to 10 with a step of 2

array_arange = np.arange(0, 10, 2)
print(array_arange) 

# Create an array of 5 evenly spaced values between 0 and 10
array_linspace = np.linspace(0, 10, 5)
print(array_linspace) 

# Q.11 How do you create an array filled with zeros or ones?			


# we can create an array filled with zeros or ones in NumPy using 
# the numpy.zeros() and numpy.ones() functions. 

# Create a 2D array of zeros
zeros_2d = np.zeros((2, 3))  # 2 rows and 3 columns
print(zeros_2d)

# Create a 2D array of ones
ones_2d = np.ones((3, 2))  # 3 rows and 2 columns
print(ones_2d)		

# Q.12 Why do we need statistical functions 		
# Answer
'''Statistical functions are integral to converting raw data into actionable insights. 
They help individuals and organizations make informed decisions, 
validate hypotheses, and understand complex phenomena across various fields. 
Understanding and applying these functions can greatly 
enhance analytical capabilities and outcomes.
'''

# Q.13 WAP  for variance, std deviation	

array = np.array([1, 2, 3, 4])

variance = np.var(array)
std_deviation = np.std(array)

print("Variance of array is :", variance)
print("Standard Deviation of array is :", std_deviation)
print()




