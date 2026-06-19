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

#arange is a function which is used to create an array of numbers.
#Syntax :- np.arange(start, stop , step)

shau6 = np.arange(1,10,2) #Here it mean we want array from 1 to 10 but with step of 2
print(shau6)

#linspace is a function which divide the equal number of space between the values.
#Syntax:- np.linspace(1,20,10) #Here 1 is start value , 20 is end value and 10 is number of space.
shau7 = np.linspace(1,20,10)
print(shau7)
# #Output will be :- [ 1.          3.11111111  5.22222222  7.33333333  9.44444444 11.55555556
#  13.66666667 15.77777778 17.88888889 20.        ]

#shape function is used to describe the shape of the array.
#Syntax:- var_name.shape
shau8 = np.array([[1,2,3,4,5,6],
                  [7,8,9,10,11,12]])
print(shau8.shape) #Output will be :- (2,6)


shau9 = np.array([1,2,3,4,5,6])
print(shau9.shape) #Output will be :- (6,)


#reshape function is used to convert the array dimension to another dimension
# Syntax:- var_name.reshape(row, column, number of element).
shau10 = np.array([1,2,3,4,5,6])
print(shau10.reshape(2,3))
#number of element matters in conversion.



sh = np.array([1,2,3,4,5,6,7,8])
print(sh.reshape(8,1))


sha = np.array([[1,2,3],
                [4,5,6]])
print(sha.reshape(6,))
#If we have many elements in array and we can't count easily so we can use -1, for reshaping any 2d or 3d into 1d.
shaa = np.array([[1,2,3],
                [4,5,6]])
print(shaa.reshape(-1,))

#Creating array with Ones and Zeros
#For Ones
#syntax:- np.ones(args)
a = np.ones(10)
print(a) #Output will be :- [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

#If we want in 2d or 3d then:-
#Syntax:- np.ones((row, column))
b = np.ones((2,3))
print(b) #Output will be :- [[1. 1. 1.]
       #                  [1. 1. 1.]]
#For Zeros
#syntax:- np.zeros(args)
b = np.zeros(10)
print(b) #Output will be :- [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#If we want in 2d or 3d then:-
#Syntax:- np.zeros((row, column))
b = np.zeros((2,3))
print(b) #Output will be :- [[0. 0. 0.]
       #                  [0. 0. 0.]]
       
       
#Array with Array Operations:-
#Arithmetic Operations
#Relational Operations
#Logical Operations
#Bitwise Operations
#Membership Operations
#Identity Operations

#1. Arithmetic Operations:- 
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 % arr2)
print(arr1 ** arr2)
shau = np.array([10,20,30])
print(shau>>3)
print(shau&4)
print(shau//10)
print(shau%10)
print(shau**4)
print(shau << 2)
res = shau.all and 11
print(res)

#Array with Inbuilt functions:-
#1. max()
#2. min()
#3. sum()
#4. abs()
#5. mean()
#6. std()
#7. median()
print(max(shau))
print(min(shau))
print(sum(shau))
print(np.mean(shau))
print(np.median(shau))
print(shau.mean())
print(shau.argmax())
print(abs(shau))
print(np.std(shau))