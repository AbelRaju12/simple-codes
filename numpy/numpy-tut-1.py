import numpy as np

zero_array = np.zeros((2, 3, 3))
# print(zero_array)

one_array = np.ones((2,2,2), dtype = 'int32') #dype not necessary
# print(one_array)

b = np.array([[[2, 3, 4], [5, 6, 7]], [[5, 7, 9], [3, 2, 1]]])

c = np.full_like(b, 5) #prints the b matrix with value 4
# print(c)

random_array = np.random.random_sample(b.shape)
random_array = np.random.rand(3, 3, 3)
random_array = np.random.randint(0,20, size = (3, 3)) #0,20/simply 20 is the limit
# print(random_array)

identity_mat = np.identity(4)
# print(identity_mat)

arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis = 0)
# print(r1)

# we want to intialize
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1 
# 1 0 0 0 1
# 1 1 1 1 1

req_mat = np.ones((5, 5))
manip_mat = np.zeros((3, 3))
manip_mat[1, 1] = 9
req_mat[1:4, 1:4] = manip_mat #1:4 #1 is row and #2 is coloumn
# print(req_mat)

a = b.copy() #use copy() instead of just assingnment else manipulating a => manipulates b

# all basic arithemtic matrix operations like add mult, sub, div
# print(b ** 2)