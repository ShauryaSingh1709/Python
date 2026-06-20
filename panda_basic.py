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