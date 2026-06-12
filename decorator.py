#Syntax :- 
# def <decorator_name>(func):
#     def wrapper(*args, **kwargs):
#         pre task
#         func(*args, **kwargs)
#         post task
#     return wrapper





def my_decorator (func):
    def wrapper():
        print("This is start of decorator")
        func()
        print("This is end of decorator")
    return wrapper
@my_decorator
def greet():
    print("Hello World")
greet()
#First Concept to call decorator.
def shaurya (func):
    def wrapper():
        print("This is start of decorator")
        func()
        print("This is end of decorator")
    return wrapper
@shaurya
def greet():
    print("Hello World")
greet()
#Second concept to call decorator.
def shaurya (func):
    def wrapper():
        print("This is start of decorator")
        func()
        print("This is end of decorator")
    return wrapper
def greet():
    print("Hello World")
x = shaurya(greet)
x()
