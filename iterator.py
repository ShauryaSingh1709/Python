#Iterator :- It is the process of traversing through sequence and getting the value one by one.
# The function is used to perform iteration.
# For loop is completely depend on iterator so that it has an inbuilt iterator.
# To perform iterator it consist of two important method :- iter() and next()
a = [1,2,3,4]
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) #This will give error bcoz list is exhausted stopiteration error.
print(it) #give address.

#Iter() method :- It is a function which is used to make the control to get pointed to the initial node address.
#Syntax for iter() is :- var_name = iter(iterable)
