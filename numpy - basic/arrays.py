import numpy as np

test_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
test_matrix = [["a","b","c"],["d","e","f"],["g","h","i"]]

#casting list to numpy array & matrix
np_arr = np.array(test_data)
np_matrix = np.array(test_matrix)

#create np array with numpy with step size
np_arr = np.arange(0,10,2)

#array of zeros & matrix array of zeros 5 by 5 same goes for arrays of ones
zero_arr = np.zeros(3)
zero_matrix = np.zeros((5,5))

#linspace returns array of evenly spaced points that you declare in some range 
lin_arr = np.linspace(0,100,100)

#random arrays
#uniform distribution of 5 
rand = np.random.rand(5)
#normal distribution 
rand = np.random.randn(5)
#random numbers form lowest to highest with size
rand = np.random.randint(1,100,20)

#reshaping np array into matrix 
np_arr = np.arange(25)
np_to_matrix = np_arr.reshape(5,5)

#find min/max value & index in array 
np_arr = np.random.randint(0,50,10)
max_np = np_arr.max()
max_np_index = np_arr.argmax()
min_np = np_arr.min()
min_np_index = np_arr.argmin()

#shape of array 
np_arr.shape
#datatype of array 
np_arr.dtype
#array of true false based on if statment 
bool_array = np_arr > 3
#array of numbers that are bigger than 3
np_arr2 = [np_arr > 3]

