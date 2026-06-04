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

#WAP to subtract three numbers using lambda function.
a = lambda a,b,c: a-b-c
print(a(10,20,30))
#Another way:-
print((lambda a,b,c: a-b-c)(10,20,30))

#WAP to check whether the number is greater or not using lambda function and if number is greater print "HYE" else print "BYE".
a = lambda a,b: "HYE" if a > b else "BYE"
print(a(40,20))

#Second way :-
print((lambda a,b: "HYE" if a > b  else "BYE")(10,20))


#WAP to print cube if value is odd or else square of that number

a = lambda a: "cube" if a % 2 != 0 else a*a
print(a(5))

#WAP to find the greatest number among three number
a = lambda a,b,c: "A is greater" if a > b and a > c else "B is greater" if b > a and b > c else "C is greater"
print(a(10,20,30))

#WAP to check number is negative positive or zero
a = lambda a: "Number is positive" if a > 0 else "Number is Negative" if a < 0 else "Number is zero"
print(a(0))

#WAP to calcuate area of rectangle
a = lambda l,b: l*b
print(a(10,20))


#WAP to calculate the simple intrest
a = lambda a,b,c: (a*b*c)/100
print(a(10,200,300))