#Numpy is used to perform mathematical operations.
#Numpy is a library which is used to work with arrays.
#Numpy is a library which is used to work with matrices.

import numpy as np #np is alias for numpy.
# np.__version__ #to get the version of numpy.
b = np.array([1,2,3,4])
print(b) #to print the array

#np.ndim is a function which is used to get the dimension of the array.
print(b.ndim)

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([7,8,9,10,11,12]) 
#this is how we create array in numpy.

#In Numpy we have three types of Arrays:
#1. 1D Array (Unidimensional Array)
#2. 2D Array (Bidimensional Array)
#3. 3D Array (Multidimensional Array)

#1D Array (Unidimensional Array)
arr1 = np.array([1,2,3,4,5,6])
print(arr1)

#2D Array (Bidimensional Array)
arr2 = np.array([[1,2,3,4,5,6],
                 [7,8,9,10,11,12]])
print(arr2)
print(arr2.ndim)

#3D Array (Multidimensional Array)
arr3 = np.array([[[1,2,3,4,5,6],
                  [7,8,9,10,11,12]],
                 [[13,14,15,16,17,18],
                  [19,20,21,22,23,24]]])
print(arr3)
print(arr3.ndim)

#dtype is a function which is used to get the data type of the array.
#Syntax :- var_name.dtype
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)


#astype is a function which is used to change the data type of the array.
#Syntax :- var_name.astype(data_type)
shau = np.array([1,2,3,4,5,6,7])
shau.dtype
print(shau)
shau1 = shau.astype(float)
print(shau1)
shau1.dtype


#If we want to change any array permanently then :-
shau5 = np.array([1,2,3,4,5,6],dtype=float)
shau5.dtype
print(shau5)
#This is how we can permanently changed the data type of the array.

