#File Handling :- 
#1. It is the process of writing the data into the file or reading the data from the file.
#2. File is the container which is used to store the data.
#3. Based on the file extension it is possible to identify the type of data stored in a file.
#4. Before handling any file getting accessibility is mandatory.
#5. In python open() function is used to get the accessibility of a file before that we have to follow the syntax.
#Syntax:-  
#var_name = open('path/filename', 'mode')   #Syntax 1
#with open('path/fname', 'mode') as var #synatx 2
#6. In the mode of operation writing the data into the file or reading from the file for that we have to use modes.
#7. Mode of operation classified into three types:- 
#a. write()
#b. read()
#c. append()


#1:- Write() :- Write mode is used to write the content into the file.
#If file is not present then write mode will create the file.
#If file exist then content will override.
# Write mode has two function
#a. write()
#b. writeline() 
#c. w+
#Syntax for writeline() :-
# f.writeline([iterable of collection])
f = open('sample.txt', 'w')
# f.write('This is file handling')
f.write('Hello This is Shaurya\n')
f.writelines(['1.Python\n', '2.GO lang'])
f.close()

f = open('bestf.txt', 'w')
f.write('1.My bestf is my bestf\n')
f.write('2.Bestf is only my Bestf\n')
f.write('3.Bestf is only my Bestf\n')
f.write('4.Bestf is only my Bestf\n')
f.close()


#2:- Read() :- It is used to read the data from the file.
#In this case if file is not exist then controller wil throw error.
#In read mode we have three types of operations :-
#a. read()
#b. readline()
#c. readlines()
f = open('sample.txt', 'r')
print(f.read()) #This will give full file
f.close()

f = open('sample.txt', 'r')
print(f.read(10)) #This will print first 10 char ex:- Hello This
f.close()

f = open('sample.txt', 'r')
print(f.read(10)) #This will print first 10 char ex:- Hello This
print(f.read(10)) #This will print next 10 char from Hello This , ex:-  is Shaury
f.close()


f = open('sample.txt', 'r')
print(f.read(10)) #This will print first 10 char ex:- Hello This
print(f.read(10)) #This will print next 10 char from Hello This , ex:-  is Shaury
print(f.readline()) #This will print full first line.
f.close()


f = open('sample.txt', 'r')
print(f.readlines()) #Output:- ['Hello This is Shaurya\n', '1.Python\n', '2.GO lang']
f.close()

#3. Append():- Append mode is almost similar to write mode but if file is already exist then controller will add a new data to the exisiting file without performing overriding.
# In append we have two types of function:-
#a. write()
#b. writeline()

#Syntax :- var = open('path/fname', 'a')
f = open('sample.txt', 'a')
f.write("\nHello new here")
f.close()


#tell():- 
f = open('sample.txt', 'a')
print(f.tell())
f.close()

#seek():-
f = open('sample.txt', 'a')
print(f.tell()) #Output:- 58
f.seek(5) #We set it to 5
print(f.tell()) #Output:- 5
f.close()