# numpy is faster and efficient than lists. It uses contigous memory. Several apps like mathematics, plotting, bk-end, ml 
import numpy as np

a = np.array([[1, 2, 3, 6, 8, 9, 10],[4, 5, 6, 3, 2, 3, 3]])

# # get dimension
# dimension = a.ndim
# print(dimension)

# # get shape
# shape = a.shape
# print(shape) #2x3

# # get type
# type = a.dtype
# print(type)


# # get size
# size = a.itemsize
# print(size)


# # get total size
# tot_size = a.nbytes
# print(tot_size)

# print(a[1, 5]) #to get 3rd row and 5th col element
# a[1, 5] = 20
# print(a[1,5])

# # To get a specific row/ coloumn

# print(a[0 , :])
# print(a[:, 5])

# print(a[1, 0: -2: 2])

b = np.array([[[2, 3, 4], [5, 6, 7]], [[5, 7, 9], [3, 2, 1]]])
# print(b)