#Exception Handling 
#1. try:
#2. except:
# a = int(input("Enter a value"))
# b = int(input("Enter another value"))
# print(a/b)
#If we put a = 10 and b = 0 then it will give ZeroDivisionError: division by zero
#So we will use exception handling:-
try:
    a = int(input("Enter a value "))
    b = int(input("Enter another value "))
    print(a/b)
except ZeroDivisionError:
    print("Error hai bhai 0 pass nhi kro") #This will give output as Error hai bhai 0 pass nhi kro
except ValueError:
    print("Pass number bro not alphabetic value") #If we will give a b c or anything rather than number than we need this too.