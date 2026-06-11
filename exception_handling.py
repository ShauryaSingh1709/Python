#Exception Handling 
#1. try:
#2. except:
# a = int(input("Enter a value"))
# b = int(input("Enter another value"))
# print(a/b)
#If we give input a = 10 and b = 0 then it will give ZeroDivisionError: division by zero
#So we will use exception handling:-
try:
    a = int(input("Enter a value "))
    b = int(input("Enter another value "))
    print(a/b)
except ZeroDivisionError:
    print("Error hai bhai 0 pass nhi kro") #This will give output as Error hai bhai 0 pass nhi kro
except ValueError:
    print("Pass number bro not alphabetic value") #If we will give input as a b c or anything rather than number than we need this too.
    
#Exception Handling consist of three types:-
#1. Specific Exception Handling
#2. Generic Exception Handling
#3. Default Exception Handling
# Default exception Handling have two parts:-
#a. Custom Exception Handling.
#b. User defined Exception Handling.


#SPECIFIC EXCEPTION HANDLING:- When we know the type of error we gonna face then we use specific exception handling.
#Example:-
try:
    a = int(input("Enter a value "))
    b = int(input("Enter another value "))
    print(a/b)
except ZeroDivisionError:
    print("Error hai bhai 0 pass nhi kro") 
except ValueError:
    print("Pass number bro not alphabetic value")
    
#Create a specific exception handling where we have to handle zerodivision error , value error and key error.
try:
    a = int(input("Enter a value "))
    b = int(input("Enter another value "))
    print(a/b)
    c = {"a":1, "b":2, "c":3}
    print(c["d"])
except ZeroDivisionError:
    print("Error hai bhai 0 pass nhi kro") 
except ValueError:
    print("Pass number bro not alphabetic value")
except KeyError:
    print("Key Error")


#GENERIC EXCEPTION HANDLING:- 
try:
    a = int(input("Enter a value "))
    b = int(input("Enter another value "))
    print(a/b)
except Exception:
    print("Sorry Error Occured")
    
    
#DEFAULT EXCEPTION HANDLING:-

# while True:
#     print("hi") #This will go infinity and infinity and when we will stop then it will give keyboard interrupt error.
    
try:
    while True:
        print("Hi")
except:
    print("Sorry Error Occured") #This will avoid keyboard interrupt error.


#Custom Exception Handling:- 
#Syntax:- raise <exception> ("message")

#User defined exception handling:-
#Syntax:- 
#class Error_name(Exception):
#   pass
#raise Error_name("message")
class AgeError(Exception):
    pass
try:
    age = int(input('Enter the age '))
    if age < 18:
        raise AgeError('Not eligible')
    else:
        print('Eligible')
except AgeError as E:
    print(E)
    
    
#finally:-
#Syntax:-
# try:
#     S.B
# except:
#     S.B
# except:
#     S.B
# finally: #finally will always execute.
#     S.B  
try:
    a = int(input("Enter a value"))
    b = int(input("Enter another value"))
    print(a/b)
except ZeroDivisionError:
    print("Error hai bhai 0 pass nhi kro") 
finally:
    print("Code executed succesfully")
    