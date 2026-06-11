#random :- 
#1. random()
#2. randint()
#3. choice()
#4. shuffle()
#5. sample()

import random
print(random.random()) #It will give random value between the range of 0.0 to 1.0

# print(random.randint(start value , end value))
print(random.randint(1,6)) #It will give random value between the range of start value to end value. start value must be smaller than end value.


# print(random.choice(iterable))
l = 1,2,3,4,5,6
print(random.choice(l)) #It will give random value from the list.

a = ['apple', 'mango', 'banana', 'grapes']
print(random.choice(a)) 

#(random.shuffle(iterable))
#print(iterable) to check shuffle list.
abc = ['apple', 'mango', 'banana', 'grapes']
(random.shuffle(abc)) #It will shuffle the list.
print(abc)

#sample(iterable, k)
shau = ['apple', 'mango', 'banana', 'grapes']
print(random.sample(shau, 2))



import math

print(math.ceil(4.7)) #output :- 5
print(math.floor(4.7)) #output :- 4
print(math.pow(2,3)) #output :- 8 here 2 will base and 3 will power
print(math.factorial(5)) #output :- 120
print(math.isqrt(726)) #output :- 26
print(math.sqrt(726))  #output :- 26.94438717061496
print(math.sqrt(144)) #output :- 12.0
print(math.isqrt(144)) #output :- 12
print(math.gcd(12,18)) #output :- 6
print(math.lcm(12,18)) #output :- 36
print(math.pi) #output :- 3.141592653589793
print(math.log(100)) #output :- 4.605170185988092
print(math.log10(100)) #output :- 2.0