#MAP()
#It is a function which is used to perform same set of opertion for each and every value present inside the collection.
#Syntax:- 
#map(collection, function)
#Example
a = [1,2,3,4]
b = map(lambda x: x*x, a)
print(list(b))

#WAP to convert into uppercase.
sh = ['aman', 'rahul', 'sumit']
b = map((lambda x: x.upper()), sh)
print(list(b))