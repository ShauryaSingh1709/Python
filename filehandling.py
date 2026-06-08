#File Handling :- 
#1. It is the process of writing the data into the file or reading the data from the file.
#2. File is the container which is used to store the data.
#3. Based on the file extension it is possible to identify the type of data stored in a file.
#4. Before handling any file getting accessibility is mandatory.
#5. In python open() function is used to get the accessibility of a file before that we have to follow the syntax.
#Syntax:-  
#var_name = open('path/filename', 'mode')   #Syntax 1
#open('path/fname', mode) as var #synatx 2
#6. In the mode of operation writing the data into the file or reading from the file for that we have to use modes.
#1:- Write() :- Write mode has two mode 
#a. write()
#b. writeline() 
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