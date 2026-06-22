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

#If we have to change the index then we have to change like this:-
shaurya = pd.Series([1,2,3,4,5])
shaurya.name = "Weight in Kg"
fruit = ["Banana", "Apple", "Mango", "Strawberry", "Orange"]
shaurya.index = fruit
print(shaurya)
#Output:-
'''
Banana      1
Apple       2
Mango       3
Strawberry  4
Orange      5
Name: Weight in Kg, dtype: int64
'''
fruit = ["Banana", "Mango", "Apple", "Strawberry", "Orange"]
shaurya.index = fruit
shaurya
#Here we have chnaged the index of shaurya
#Output:- 
'''
Banana      1
Mango       3   
Apple       2
Strawberry  4
Orange      5
Name: Weight in Kg, dtype: int64
'''
#This is how we changed the index of apple and mango.
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
#If we don't want True or False just want to get True values then we will do it like:-
print(shauu[shauu>5])
#Output:- 
'''
Mutton    10
Fish      15
Egg       20
Name: Protein in Grams, dtype: int64
'''

#Logical Operators:-
#1. And (&)
#2. Or (or)
#3. Not (not)

#1. And (&)
print(shauu[(shauu>5) & (shauu<16)])
#Output:-
'''
Mutton    10
Fish      15
Name: Protein in Grams, dtype: int64
'''
#This will return any value which is greater than 5 and less than 16

#2. Or (or)
print(shauu[(shauu>5) | (shauu<16)])
#Output:-
'''
Milk       5
Mutton    10
Chicken     4
Fish      15
Egg       20
Name: Protein in Grams, dtype: int64
'''
#This will return any value which is greater than 5 or less than 16

#3. Not (not)
print(shauu[~(shauu>5)])
#Output:-
'''
Milk       5
Chicken     4
Name: Protein in Grams, dtype: int64
'''
#This will return any value which is not greater than 5

#Modification of series:-
shauu["Chicken"] = 6
print(shauu)

#Dataframe:-
#A dataframe is a 2D array of data, similar to a spreadsheet, with rows and columns.
#Creating a Dataframe:-

#Syntax:- var = pd.DataFrame(dict)

import pandas as pd
a = { 'sname': ['Rahul', 'Shaurya', 'Aman'],
      'Rollno': [1,2,3],
      'marks': [10,20,30],
      'mock': ['a','b','c']}
meow = pd.DataFrame(a)
print(meow)
#Output:- 
'''
   sname  Rollno  marks mock
0  Rahul       1     10     a
1 Shaurya      2     20     b
2   Aman       3     30     c
'''

#Output in google colab or notebook :- 
'''	
sname	Rollno	marks	mock
0	Rahul	1	10	      a
1	Shaurya	2	20	      b
2	Aman	3	30	      c    #With edit option of dataframe.
''' 
#And code for google colab or notebook is :-
# import pandas as pd
# a = { 'sname': ['Rahul', 'Shaurya', 'Aman'],
#       'Rollno': [1,2,3],
#       'marks': [10,20,30],
#       'mock': ['a','b','c']}
# meow = pd.DataFrame(a)
# meow

#How to access only column of a Dataframe:-
print(meow["sname"])
#output :- 
'''
0    Rahul
1  Shaurya
2    Aman
Name: sname, dtype: object
'''
#How to add new column:-
meow['Branch'] = ['AIDS', 'CYS', 'CSE']
print(meow)
#Output:-
'''
   sname  Rollno  marks mock Branch
0  Rahul       1     10     a   AIDS
1 Shaurya      2     20     b    CYS
2   Aman       3     30     c    CSE
'''
#How to access any thing like we want to access AIDS:-
print(meow["Branch"][0])
#Output:-
'''
AIDS
'''

#Create a Dataset with 5 column and ten elements and access them:-
dataset = { 'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
      'Rollno': [1,2,3,4,5,6,7,8,9,10],
      'marks': [10,20,30,40,50,60,70,80,90,100],
      'Section': ['a','b','c','d','e','f','g','h','i','j'],
      'Branch': ['AIDS', 'CYS', 'CSE', 'AIDS', 'CYS', 'CSE', 'AIDS', 'CYS', 'CSE', 'AIDS']}
Shaurya = pd.DataFrame(dataset)
print(Shaurya)
#Output :- 
'''
    name    Rollno       marks      Section        Branch
0     A       1          10          a             AIDS
1     B       2          20          b             CYS
2     C       3          30          c             CSE
3     D       4          40          d             AIDS
4     E       5          50          e             CYS
5     F       6          60          f             CSE
6     G       7          70          g             AIDS
7     H       8          80          h             CYS
8     I       9          90          i             CSE
9     J      10         100          j             AIDS
'''
#Access name of topper:-
print(Shaurya['name'][9]) 
#Output:- #J
#Access marks of topper:-
print(Shaurya['marks'][9])
#Output:- #100
#Access Branch of topper:-
print(Shaurya['Branch'][9])
#Output:- #AIDS
#Access Section of topper:-
print(Shaurya['Section'][9])
#Output:- #j

#Using Amazon Dataset for learning:- 
meow1 = pd.read_csv('./Datasets/amazon_fires.csv', encoding = 'ISO-8859-1')
print(meow1)

#head():- To access first 5 elements:-
print(meow1.head())
#If 
print(meow1.head(10)) #Then it will give first then elements

#tail():- To access last 5 elements:-
print(meow1.tail())

#If we want to access any column's with n number of elements then:-
print(meow1['mes'].head(20))
#This will give output as :-
'''
     mes
0    Janeiro
1    Janeiro
2    Janeiro
3    Janeiro
4    Janeiro
5    Janeiro
6    Janeiro
7    Janeiro
8    Janeiro
9    Janeiro
10   Janeiro
11   Janeiro
12   Janeiro
13   Janeiro
14   Janeiro
15   Janeiro
16   Janeiro
17   Janeiro
18   Janeiro
19   Janeiro
'''

#info():- To access information about the dataset:-
print(meow1.info())
#Output:-
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6454 entries, 0 to 6453
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   ano       6454 non-null   int64 
 1   mes       6454 non-null   object
 2   estado    6454 non-null   object
 3   numero    6322 non-null   object
 4   encontro  6454 non-null   object
dtypes: int64(1), object(4)
memory usage: 252.2+ KB
'''

#describe():- To access Mathematical information of the dataset:-
print(meow1.describe())
#Output:-
'''
          ano
count  6454.0
mean   2014.0
std       0.0
min    2014.0
25%    2014.0
50%    2014.0
75%    2014.0
max    2014.0
'''

#To perform describe on particular column:-
print(meow1['ano'].describe())
#Output:-
'''
count    6454.0
mean     2014.0
std        0.0
min    2014.0
25%    2014.0
50%    2014.0
75%    2014.0
max    2014.0
Name: ano, dtype: float64
'''

#If we want to get information about any particular column then :-
print(meow1['mes']=='Janeiro')
#This will return only true false but if we want data then :-
print(meow1[meow1['mes']=='Janeiro']) #This is known as boolean filteration.

#Ques - Fetch the data of mes should be janeiro and estado should be Acre
print(meow1[(meow1['mes']=='Janeiro') & (meow1['estado']=='Acre')])
#Output:-
'''
[541 rows x 5 columns]
     ano      mes estado    numero  encontro
0   1998  Janeiro   Acre   0 Fires  1/1/1998
1   1999  Janeiro   Acre   0 Fires  1/1/1999
2   2000  Janeiro   Acre   0 Fires  1/1/2000
3   2001  Janeiro   Acre   0 Fires  1/1/2001
4   2002  Janeiro   Acre   0 Fires  1/1/2002
5   2003  Janeiro   Acre  10 Fires  1/1/2003
6   2004  Janeiro   Acre   0 Fires  1/1/2004
7   2005  Janeiro   Acre  12 Fires  1/1/2005
8   2006  Janeiro   Acre   4 Fires  1/1/2006
9   2007  Janeiro   Acre   0 Fires  1/1/2007
10  2008  Janeiro   Acre   0 Fires  1/1/2008
11  2009  Janeiro   Acre   0 Fires  1/1/2009
12  2010  Janeiro   Acre   1 Fires  1/1/2010
13  2011  Janeiro   Acre   0 Fires  1/1/2011
14  2012  Janeiro   Acre   0 Fires  1/1/2012
15  2013  Janeiro   Acre   0 Fires  1/1/2013
16  2014  Janeiro   Acre   0 Fires  1/1/2014
17  2015  Janeiro   Acre   1 Fires  1/1/2015
18  2016  Janeiro   Acre  12 Fires  1/1/2016
19  2017  Janeiro   Acre   0 Fires  1/1/2017
'''