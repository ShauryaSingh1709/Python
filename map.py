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


# Question 1: Square and Cube Together
# Given a list of numbers, use map() and lambda to create a new list containing the square
# and cube of each number as a tuple.
# Input: [1, 2, 3, 4]
# Expected Output: [(1, 1), (4, 8), (9, 27), (16, 64)]

i = [1, 2, 3, 4]
b = map(lambda x,y: (x*x ,y*y*y) ,i, i)
print(list(b))


# Question 2: Calculate GST
# Given a list of product prices, add 18% GST to each price using map() and lambda.
# Formula : price + (price * 18 / 100)
# Input: [100, 250, 500]
# Expected Output: [118.0, 295.0, 590.0]

sh =  [100, 250, 500]
b = map(lambda x: x + (x * 18)/ 100, sh)
print(list(b))



# Question 3: Extract Last Character
# Given a list of names, extract the last character of each name.
# Input: ['Rahul', 'Aman', 'Priya']
# Expected Output: ['l', 'n', 'a']

shau = ['Rahul', 'Aman', 'Priya']
b = map(lambda x: x[-1], shau)
print(list(b))

# Question 4: Convert Seconds to Minutes
# Convert each value from seconds to minutes.
# Input: [60, 120, 180, 300]
# Expected Output: [1.0, 2.0, 3.0, 5.0]

time = [60, 120, 180, 300]
b = map(lambda x: x/60, time)
print(list(b))


# Question 5: Add Elements of Three Lists
# Add corresponding elements of three lists using a single map() and lambda.
# Input: a=[1,2,3], b=[4,5,6], c=[7,8,9]
# Expected Output: [12, 15, 18]
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
bc = map(lambda x,y,z: x+y+z, a,b,c)
print(list(bc))

# Question 6: Even or Odd
# Return Even if the number is even, otherwise Odd.
# Input: [10, 15, 20, 25]
# Expected Output: ['Even', 'Odd', 'Even', 'Odd']

l = [10, 15, 20, 25]
lam = map(lambda x: "Even" if x%2 == 0 else "Odd" , l)
print(list(lam))


# Question 7: Find Length of Each Word
# Find the length of each word using map() and lambda.
# Input: ['python', 'java', 'react', 'django']
# Expected Output: [6, 4, 5, 6]

long = ['python', 'java', 'react', 'django']
shaurya = map(lambda x: len(x), long)
print(list(shaurya))

# Question 8: Calculate Net Salary
# Deduct 10% tax from each salary.
# Input: [30000, 45000, 60000]
# Expected Output: [27000.0, 40500.0, 54000.0]

blah = [30000, 45000, 60000]
shauryaaaaaa = map(lambda x: x - (x*10)/100 , blah)
print(list(shauryaaaaaa))


# Question 9: Reverse Each String
# Reverse each string using map() and lambda.
# Input: ['python', 'java', 'react']
# Expected Output: ['nohtyp', 'avaj', 'tcaer']

blah1 = ['python', 'java', 'react']
shauryaaaaaaa = map(lambda x: x[::-1] , blah1)
print(list(shauryaaaaaaa))


# Question 10: Student Grade Calculator
# Return grades A/B/C/Fail based on marks.
# Input: [95, 72, 55, 35, 88]
# Expected Output: ['A', 'B', 'C', 'Fail', 'A']

blah2 = [95, 72, 55, 35, 88]
shauryaaaaaaaa = map(lambda x: "A" if x >= 85 else "B" if x >= 70 else "C" if x >= 50 else "Fail", blah2)
print(list(shauryaaaaaaaa))


# Challenge Question
# Using only map() and lambda, create:
# ['Rahul-Pass', 'Aman-Pass', 'Priya-Pass', 'Neha-Fail']

alavya = ["Rahul", "Aman", "Priya", "Neha"]
marks = [85, 72, 55, 35]
shauryaaaaaaa = map(lambda y,x: (y + "-Pass") if x > 50 and x < 100 else (y + "Fail") , alavya, marks)
print(list(shauryaaaaaaa))