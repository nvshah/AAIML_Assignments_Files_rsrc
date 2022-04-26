import numpy as np

import math

# # 1) axis param concept (axis is often used with the reduce function)
# l = [
#     [[1,0], [2,1]],
#     [[0,1], [3,5]],
# ]

# arr = np.array(l)

# print(arr.ndim)
# print(arr.shape)

# sum_depth_0 = np.sum(arr, axis=0) # Depth-Wise
# sum_depth_1 = np.sum(arr, axis=1) # Height(Column)-Wise
# sum_depth_2 = np.sum(arr, axis=2) # Widht(Row)-Wise

# print(sum_depth_0, sum_depth_1, sum_depth_2, sep='\n')

# # -----

# # 2) newaxis, (add one more axis to dimen)

# arr = np.arange(1,5)
# print(arr.ndim, arr.shape) # 1 (4,)
# arr = arr[:, np.newaxis]  # Convert 1D array to 2D array
# print(arr.ndim, arr.shape) # 2 (4, 1)

# # ------

# # 3)  use of newaxis : (BroadCasting Example)

# arr1 = np.arange(1,5)
# arr2 = np.arange(10,40,10)

# #arr3 = arr1 + arr2 # Error : operands could not be broadcast together with shapes (4,) (3,) 

# # Trick
# arr3 = arr1[:, np.newaxis] + arr2 
# print(arr3)
# '''
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]
#  [14 24 34]]
# '''

# # ---------------
# # 4 rehsape

# a = np.array([[1,2,3],[4,5,6]])
# b = a.reshape((3,2))
# print(b)
# b[2, 0] = 50  # replacing the 5 with 50
# print(a[1, 1])   # 50, :- Magic in a also it gets updated i.e reshape only returns the `View`

# # Another Example - reshape() returns View | Proof

# a = np.array([[1],[2]]) # (2,1)
# b = a.reshape((1,2))  # (1,2)
# b[0,1] = 3
# print(b)   # [[1 3]]
# print(a[1, 0]) # 3    , MAGIC

# # Eg 3
# a = np.array([[1],[2]]) # (2,1)
# b = a.T 
# c = b.reshape((2,1))
# c[1,0] = 30
# print(b[0,1])  # 30
# print(a[1,0])  # 30

# # print(a)
# # print(b)
# # print(c)

# # Eg 4 rehsape may also return a copy
# a = np.array([[1],[2]]) # (2,1)
# b = a.T 
# c = b.reshape(2*1)   # Convert a Matrix to a Vector
# c[0] = 100
# print(c)
# print(b)
# print(a)

# # ---------------------------SHORT TRICKS-----------------------------

# # ---------
# # Convert a matrix to a vector

# a = np.array([[1,2,3], [4,5,6]])
# b = a.reshape(-1)  # inferred automatically
# c = a.reshape(math.prod(a.shape))  # manual calculation
# print(b)
# print(c)


# #----------
# # Gnerate any shape matrix

# a = np.arange(4*2*1).reshape((4,2,1))  # generate 4*2*1 matrix
# print(a)

# #------------
# # resize() amazing fact 

# a = np.arange(3)
# a.resize((2, 3))  # resize is inplace modification

# print(a) # will work

# a = np.array([1,2,3])
# b = a[:]
# a.resize((2,3))  # Error -> cannot resize an array that references or is referenced

# # -----------
# # Get Sorted Element from Sorted Indices (argsort() + list indexing)

# a = np.array([4,2,5,3,1])
# b = a[np.argsort(a)]   # a[[4, 1, 3, 0, 2]]
# print(b)  # [1 2 3 4 5]