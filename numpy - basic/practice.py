import numpy as np 

array_of_zeros = np.zeros(10)
print(array_of_zeros)

array_of_five = np.ones(10)*5
print(array_of_five)

from_to = np.arange(10,51,2)
print(from_to)

rand = np.random.randint(0,1,1)
print(rand)

rand = np.arange(0,9,1)
matrix_3 = rand.reshape(3,3)
print(matrix_3)

rand = np.arange(16,26,1).reshape(2,5)
print(rand)
#sum each column
rand1 = np.einsum('ij->j', rand)
#sum of second row
rand2 = rand[1].sum() 
print(rand2)
#sum of matrix 
print(rand.sum())
#standard deviation 
print(rand.std())