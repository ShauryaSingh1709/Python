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
# print(next(it)) #This will give error bcoz list is exhausted StopIteration error.
print(it) #give address.

#Iter() method :- It is a function which is used to make the control to get pointed to the initial node address.
#Syntax for iter() is :- var_name = iter(iterable)

#Next() method :- It is a function which is used to get the values one by one.
#Once you access all the objects inside the iterable it will give StopIteration error.
#Syntax for next() is :- next(iterator)

class Count:
    def __init__ (self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        value = self.start
        self.start += 1
        return value
counter = Count(1,10)
# print(next(counter)) this will print one by one.
for i in counter:
    print(i)