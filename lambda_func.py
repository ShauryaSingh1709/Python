#Lamda function(Anonymous function):-
#It is a function which is anonymous in nature.
#It is a function without name, which is used to declare in one single line.
#We have to make use of lambda keyword to create a lambda function.
#We can pass arguments according to the requirements.
#Syntax:-
#lambda arguments: expression
a = lambda a: a**2
print(a(10))

#Second approach:-
print((lambda a: a**2)(10))

#With two argument
a = lambda a,b: a*b
print(a(10,20))

#Example:-
a = lambda a,b,c: a+b+c
print(a(10,20,30))