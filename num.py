import numpy as np

# 1D array
arr1 = np.array([10, 20, 30, 40, 50, 60])

# Slicing the array
slice1 = arr1[1:4]  
print("Slice of 1D Array :", slice1)

# Create a 2D array
arr2 = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])

# Slicing the 2D array
slice2 = arr2[0:2, 1:3]  # Get rows 0 to 1 and columns 1 to 2
print("Slice of 2D Array :\n", slice2)

# Create a 3D array
arr3 = np.array([[[1, 2], [3, 4]], 
                 [[5, 6], [7, 8]]])

# Slicing the 3D array
slice4 = arr3[:, 1, :]  # Get all elements from the second row of each matrix
print("Slice of 3D Array :\n", slice4)

sliceA = arr3[1, :, :]  
print("All elements from Layer 1:\n", slice2)

# Modifying a slice
arr1[1:4] = 5  
print("Modified 1D Array:", arr1)

# Using negative indices
neg_slice = arr1[-3:]  
print("Last Three Elements of 1D Array:", neg_slice)

# Slicing with steps
slice3 = arr1[::2]  # for every second element
print("Every Second Element in 1D Array:", slice3)

slice2 = arr3[1, :, :]  # Get all rows and columns from Layer 1
print("All elements from Layer 1:\n", slice2)

slice5 = arr3[0, 0, 1]  # Get all rows and columns from Layer 1
print("slice5:\n", slice5)







