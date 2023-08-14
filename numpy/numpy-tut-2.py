import numpy as np

## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...

b = np.array([[[2, 3, 4], [5, 6, 7]], [[5, 7, 9], [3, 2, 1]]])

# print(np.min(b))
# print(np.sum(b, axis = 0)) # nop axis => sum of all elements
reshape = b.reshape((4, 3))
# print(reshape)

arr1 = np.array([1, 2, 4, 3])
arr2 = np.array([0, 5, 6, 8])
# print(np.vstack([arr1, arr2, arr2, arr1]))
# print(np.hstack([arr1, arr2, arr2, arr1]))


#Miscellaneous

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
# print(filedata)

# print(~((filedata > 50) & (filedata < 100)))

# print(np.all(filedata > 50, axis = 0))

