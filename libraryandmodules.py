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
