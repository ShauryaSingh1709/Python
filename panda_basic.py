#Pandas provide a simple and powerful open source data analysis and manipulation tool, built on top of the Python programming language.
#What we can do with Pandas:- 
#1. Data Cleaning
#2. Data Manipulation
#3. Data Aggregation
#4. Data Analysis
#5. Size mutabilty

#Primary Data Structure:-
#1. Series (1D)
#2. DataFrame (2D)

import pandas as pd

s = pd.Series([1,2,3,4,5])
s.name = "Shaurya"
print(s)
print(s.dtype) #This will give output as int64 as data type for this series.
print(s.values) #This will give output as [1 2 3 4 5] as values for this series.
print(s.index) #This will give output as RangeIndex(start=0, stop=5, step=1) as index for this series.
print(s.name)
#Here dtype of s is int64


a = pd.Series([1,2,3,4,5,"shaurya"])
print(a)
#Here dtype of a is object

#Indexing 
shau = pd.Series([1,2,3,4,5])
print(shau[1]) #This will give output as 2
print(shau[2]) #This will give output as 3

#If we want multiple value then :-
#Syntax:- start(included) : stop(excluded) : step
print(shau[0:3:2]) #This will give output as [1 3] because it will include 1 and then go 2 steps and then give 3 while excluding last index value..

#iloc :- Location based indexing
print(shau.iloc[0]) #This will give output as 1
print(shau.iloc[2]) #This will give output as 3

#If we want different different values then:-
print(shau.iloc[[0,2,4]]) #This will give output as [1 3 5]


shaurya = pd.Series([1,2,3,4,5])
shaurya.name = "Weight in Kg"
fruit = ["Banana", "Apple", "Mango", "Strawberry", "Orange"]
shaurya.index = fruit
print(shaurya) #This will give output as 
'''
Banana      1
Apple       2
Mango       3
Strawberry  4
Orange      5
Name: Weight in Kg, dtype: int64
''' 
#But if we using Google colab or jupyter notebook then we have to write like:-
# shaurya = pd.Series([1,2,3,4,5])
# shaurya.name = "Weight in Kg"
# fruit = ["Banana", "Apple", "Mango", "Strawberry", "Orange"]
# shaurya.index = fruit
# shaurya
#Output:- 
'''
	       Weight in Kg
Banana	      1
Apple	      2
Mango	      3
Strawberry	  4
Orange	      5
dtype: int64
'''
print(shaurya['Apple']) #This will give output as 2
#iloc used for numerical indexing so we use loc func.

#loc :- Label based indexing
print(shaurya.loc['Apple']) #This will give output as 2

#If we want multiple values then:-
print(shaurya.loc[['Apple', 'Strawberry']])
#Output:-
'''
Apple       2
Strawberry  4
Name: Weight in Kg, dtype: int64
'''

#In this type of indexing we can acess multiple values but in this start and stop value both will include.
print(shaurya["Apple":"Strawberry"])
#Output:-
'''
Apple       2
Mango       3
Strawberry  4
Name: Weight in Kg, dtype: int64
'''
#we just have to give start to end value and if we want then we can use step also.
print(shaurya["Apple":"Strawberry":2])
#Output:-
'''
Apple       2
Strawberry  4
Name: Weight in Kg, dtype: int64
'''

#Creating Series with Dictionary
Protein = {
    'Milk': 5,
    'Mutton': 10,
    'Chicken': 4,
    'Fish':15,
    'Egg':20
}
shauu = pd.Series(Protein)
shauu.name = "Protein in Grams"
print(shauu)
#Output:-
'''
Milk       5
Mutton    10
Chicken     4
Fish       15
Egg        20
Name: Protein in Grams, dtype: int64
'''

#Conditional Selection:- 
print(shauu>5)
#Output:-
'''
Milk       False
Mutton      True
Chicken    False
Fish        True
Egg         True
Name: Protein in Grams, dtype: bool
'''
#This will return any value which is greater than 5 as True else False.
