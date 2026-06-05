#Filter()
#1. It is a function which is used to get only the required data from the collection.
#2. In this case this function which we are using should return either true or false.
#3. In filter function if condition is satisfied it hold the value or else remove from the collection.



#Filter all the odd number
a = [2,4,3,5,6,7,8]
b = filter(lambda x: x%2 != 0, a)
print(list(b))

a = [2,4,3,5,6,7,8]
b = map(lambda x: x%2 != 0, a)
print(list(b))


#WAP filter number greater than 45
#Input = [100, 45, 35, 65, 66, 20, 19]
l = [100, 45, 35, 65, 66, 20, 19]
b = filter(lambda x: x>45 , l)
print(list(b))

#WAP to filter number which are negative
#Input = [1, 2, -5, 10, -11, -12]
l = [1, 2, -5, 10, -11, -12]
b = filter(lambda x: x<0 , l)
print(list(b))

#WAP to filter names which starting with A
a = ["Aman", "Rahul", "Aditya", "Lokesh", "Ambani"]
b = filter(lambda x: x[0] == "A" , a)
print(list(b))

#WAP to filter the string greater than 5 
shaurya = ["Python", "Java", "AIML", "Cyber"]
b = filter(lambda x: len(x) > 5 , shaurya)
print(list(b))


#WAP to filter number which are divisible by 3 or 5 both
a = [2,4,3,5,6,7,8,15,30,45,60]
b = filter(lambda x: x%3 == 0 and x%5 == 0, a)
print(list(b))

#WAP to filter the names which are ending with "N"
a = ["Aman", "Rahul", "Aditya", "Lokesh", "Ambani"]
b = filter(lambda x: x[-1] == "n" , a)
print(list(b))

#WAP to filter the voting age from list 
a = [15, 17, 18, 20, 14]
b = filter(lambda x: x >= 18, a)
print(list(b))

#WAP to filter palindrome words from the list
a = ["racecar", "python", "radar", "madam"]
b = filter(lambda x: x[::-1]== x, a)
print(list(b))