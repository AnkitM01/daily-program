''' Convert the below list into numpy array then display the array

 Input: my_list = [1, 2, 3, 4, 5] '''

list1 = [1,2,3,4,5]
print(list1)

# convert list into numpy

import numpy as np 

my_list = np.array([1,2,3,4,5])
print(my_list)


''' 2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

 Input: my_list = [1, 2, 3, 4, 5]'''

my_list = [1, 2, 3, 4, 5]

# Convert to numpy array
array = np.array(my_list)

# Display the array
print("Array:", array)

# Display the first and last index
print("First index:", array[0])
print("Last index:", array[- 1])

# Multiply each element by 2
result = array * 2

print("Result after multiplying by 2:", result)


import numpy as np

# Input 1D array
my_list = [1, 2, 3, 4]

# Convert to numpy array
array_1d = np.array(my_list)

# Reshape to 2x2 array
array_2x2 = array_1d.reshape(2, 2)

# Display the 2x2 array
print("2x2 Array:\n", array_2x2)




