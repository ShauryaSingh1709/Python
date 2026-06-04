#OOPs stands for Object Oriented Programming System/Structure.
#Class is a blueprint of an object.
#Object is copy or insstance of a class.

#Advantages of OOPs :-
#1. Avoid repetition of code.
#2. It is easy to maintain and modify the code.
#3. It is easy to reuse the code.
#4. It is easy to test the code.
#5. It is easy to debug the code.
#6. Make code easier to understand and use.
#7. We can organize the code properly.
#8. Solving real world problems.
#9. It is way of programming , where we have to create class and objects.

#Class :- 
# 1. Properties(Represented by variables)
# 2. Functionality(Represented by functions)
#syntax of class :-
#class classname:
#classname should be in capital letter but it's not mandatory.

#Types of class :-
#1. User defined class :- It is a class which is defined or created by the user.
#2. Built in class(Inbuilt class) :- It is a class which is predefined by the python.

#Example of user defined class :-
from pyclbr import Class


class Creation:
    a = 10
    b = 20
demo = Creation()
print(type(demo)) #Output :- <class '__main__.Creation'>
#Here __main__ is representing that class is created by the user or we can say it is a user defined class.
#Memory allocation :- 
#Method area :- It will be created into two parts :-
#1. Main Space :- Creation [0X11] and demo [0X22]
#2. Method Area :- Key and Value pair will be stored in the method area.
#key = a and b #for class Creation
#value = 10 (A1) and 20 (A2) #for class Creation and here A1 and A2 are refrence 
#Key = a and b #for object demo
#Value = A1 and A2 #for object demo

#Whenever we want to access the values from the class or object we have to use a syntax
#For class:- Cname.var
#For object;- obj.var

#Access the values of class and object :-
print(Creation.a) #Output :- 10
print(demo.a) #Output :- 10
print(Creation.b) #Output :- 20
print(demo.b) #Output :- 20

class Creation:
    a = 10
    b = 20
demo1 = Creation()
demo2 = Creation()
print(Creation.a, Creation.b) #Output :- 10 20
print(demo1.a, demo1.b) #Output :- 10 20
print(demo2.a, demo2.b) #Output :- 10 20
    

# class Shaurya:
    #Here we will define the properties and functionality of the class.
    
#Object :-
#Object is copy or instance of a class.
#Syntax of object :-
#objectname = Classname()
# shau = Shaurya() #Here shau is the object of class Shaurya.

#Example of class and object :-
class Smartphone:
    ram = 8
    rom = 256
    color = "Black"
S1 = Smartphone()
S2 = Smartphone()
print(type(S1)) #Output :- <class '__main__.Smartphone'>
#To access the properties using class
print(Smartphone.color) #Output :- Black
#To access the properties using object
print(S1.color) #Output :- Black

#To modify the properties using class
Smartphone.color = "White"
print(Smartphone.color) #Output :- White
#To modify the properties using object
S1.color = "Red"
print(S1.color) #Output :- Red

#Memory allocation of class and object :-
#Smartphone class will be stored in the memory only once but S1 and S2 will be stored in the memory separately.
#Smartphone will store ram = 8, rom = 256, color = "Black" in the memory and S1 and S2 will store the address of the class in the memory.
#Print all property of Smartphone , S1 and S2 :-
print(Smartphone.ram, Smartphone.rom, Smartphone.color) #Output :- 8 256 White
print(S1.ram, S1.rom, S1.color) #Output :- 8 256 Red
print(S2.ram, S2.rom, S2.color) #Output :- 8 256 White
#If we chnage the property of class then it will change for all the objects but if we change the property of object then it will change only for that object.


#Actual Program for Bank Data :-
class Bank:
    bname = "SBI"
    loc = "Bangalore"
    Manager = "Aditya"
cus1 = Bank()
cus2 = Bank()
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Bangalore Aditya
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Bangalore Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Bangalore Aditya
#Modification of class property :-
Bank.loc = "Chandigarh"
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Chandigarh Aditya
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Chandigarh Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Chandigarh Aditya
#Modification of object property :-
cus1.loc = "Jharkhand"
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Chandigarh Aditya
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Jharkhand Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Chandigarh Aditya

cus2.loc = "Mumbai"
print(Bank.bname, Bank.loc, Bank.Manager) #Output :- SBI Chandigarh Aditya  
print(cus1.bname, cus1.loc, cus1.Manager) #Output :- SBI Jharkhand Aditya
print(cus2.bname, cus2.loc, cus2.Manager) #Output :- SBI Mumbai Aditya

#Modification done with respect to class will affect all the objects.
#Reason:- Objects are instance/Copy of the class.


#Modification done with respect to object will not affect the class and other objects.
#Reason:- Class are not depending on the objects.

#States or Property :- 
# The data and information stored inside a class/object is known as states or property of class/object.
#                                             OR
# The variable or functionalities stored inside the class are called as states.

#There are 2 types of states or property :-
#1. Generic state/ class state/ static state.
#2. Specific state/ object state.
#-- These are the properties which will be common for every object.
#1. Generic state :- The Properties which are common for all the object are termed as generic state.
#Example for generic state :-
class School:
    sname = "CGC"
    loc = "Chandigarh"
    principal = "Aditya"
    time = "12:30-4:30"
st1 = School()
st2 = School()
print(School.sname, School.loc, School.principal, School.time) #Output :- CGC Chandigarh Aditya 12:30-4:30
print(st1.sname, st1.loc, st1.principal, st1.time) #Output :- CGC Chandigarh Aditya 12:30-4:30
print(st2.sname, st2.loc, st2.principal, st2.time) #Output :- CGC Chandigarh Aditya 12:30-4:30
#2. Object state or Specific state ;- The properties which will we create outside the class after the class creation is called as specific or object state.
#Example for object state :-
class School:
    sname = "DAV"
    loc = "Bangalore"
    principal = "Joseph Vijay"
    time = "9:00am to 12:00pm"
st1 = School()
st1.name = "Shaurya"
st1.id = 23
st1.age = 20
st1.bg = "AB+"

st2 = School()
st2.name = "Raj"
st2.id = 24
st2.age = 18
st2.bg = "O+"
print(st1.name, st1.id, st1.age, st1.bg, st1.sname, st1.loc, st1.principal, st1.time) #Output :- Shaurya 23 20 AB+ DAV Bangalore Joseph Vijay 9:00am to 12:00pm
print(st2.name, st2.id, st2.age, st2.bg, st2.sname, st2.loc, st2.principal, st2.time) #Output :- Raj 24 18 O+ DAV Bangalore Joseph Vijay 9:00am to 12:00pm


#Difference between method and function :-
#Function which we declare inside the class is called as methods.
#If we declare the function outside the class then it is called as function.

#<--example of Function-->
def add():
    print("Hello")
#add() is a function because it is declared outside the class.

#<--example of method-->
class Demo:
    def show():
        print("Hello")
#show() is a method because it is declared inside the class.

#Constructor or __init__ method or Initialisation :-
#It runs automatically when an object is created.
#It is used to initialize the member of the object.
#No need of calling the method by default it is execute when we create an object.
#self is the mandatory argument to pass for the __init__ method.
#We can pass argument in the object creation only if there is __init__ method present inside the class.
#__init__ is the constructor method in python.
#For __init__ method, passing self is mandatory to store the address of the object.
#Syntax for constructor method :-
#class Cname:
    #Block of code
    #def __init__(self, arg1, arg2, arg3,......argn):
        # self.arg1 = arg1
        # self.arg2 = arg2
        # self.arg3 = arg3
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # self.argn = argn
#Obj_name = Cname(arg1, arg2, arg3,.....argn)
#There are two types of Constructor method in python.
#1. Default/Non Parameterized Constructor
#2. Parameterized Constructor
#Arguments are actual values which are passed and value we pass while declaration of function is called parameters.
#Formal arguments = Parameters
#Actual arguments = Arguments
#Default constructor is called when we create an object without passing any argument.
#Parameterized constructor is called when we create an object by passing some argument.
#Why we use self :- It is used to refer the address of the object/ refer the object members.

class School:
    sname = "Carmel"
    loc = "Bangalore"
    principal = "Shaurya"
    timing = "9:00am to 12:00pm"
    def __init__(self, name, sid, age, bg):
        self.name = name
        self.sid = sid
        self.age = age
        self.bg = bg
st1 = School("Akanksha", 16, 24, "B+")
st2 = School("Alavya", 17, 20, "AB+")
print(st1.name, st1.sid, st1.age, st1.bg, st1.sname, st1.loc, st1.principal, st1.timing) #Output :- Akanksha 16 24 B+ Carmel Bangalore Shaurya 9:00am to 12:00pm
print(st2.name, st2.sid, st2.age, st2.bg, st2.sname, st2.loc, st2.principal, st2.timing) #Output :- Alavya 17 20 AB+ Carmel Bangalore Shaurya 9:00am to 12:00pm
    
    
#Example Question for constructor :-
#WAP to create a company having 3 class members and 1 object with 4 object member.
class Company:
    cname = "Capgemini"
    loc = "Bangalore"
    ceo = "Alavya"
    def __init__(self, ename, eid, age, bg):
        self.ename = ename
        self.eid = eid
        self.age = age
        self.bg = bg
emp1 = Company("Shaurya", 23, 20, "AB+")
print(emp1.ename, emp1.eid, emp1.age, emp1.bg, emp1.cname, emp1.loc, emp1.ceo) #Output :- Shaurya 23 20 AB+ Capgemini Bangalore Alavya

#WAP where class is Car and properties are brand, color, HP and Price make 4 object with 4 object member with different property.
class Car:
    brand = "Ferrari"
    color = "Black"
    HP = 500
    price = 1000000
    def __init__(self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
car1 = Car("Scuderia Ferrari", 500, 2022, "Red")
car2 = Car("Forza Ferrari", 600, 2023, "Yellow")
car3 = Car("Ferrari Enzo", 400, 2021, "White")
car4 = Car("Ferrari F8", 300, 2020, "Blue")
print(car1.name, car1.model, car1.year, car1.color, car1.brand, car1.HP, car1.price) #Output :- Scuderia Ferrari 500 2022 Red Ferrari 500 1000000
print(car2.name, car2.model, car2.year, car2.color, car2.brand, car2.HP, car2.price) #Output :- Forza Ferrari 600 2023 Yellow Ferrari 500 1000000
print(car3.name, car3.model, car3.year, car3.color, car3.brand, car3.HP, car3.price) #Output :- Ferrari Enzo 400 2021 White Ferrari 500 1000000
print(car4.name, car4.model, car4.year, car4.color, car4.brand, car4.HP, car4.price) #Output :- Ferrari F8 300 2020 Blue Ferrari 500 1000000

#Method :-
#1. Object Method
#2. Class Method
#3. Static Method

#Object Method :- The Method which is used to perform modification and some operation on the object member is called as object method.
#They are used to access and modify the object member.
#It is complousory to pass self to store the address of the object.
#Syntax for object method :-
#class Cname:
    #Block of code
    #def methodname(self): #To access
        #print(args)       #To access
    #def methodname(self.new):     #To modify
        #self.var = new            #To modify
#obj = Cname(val1,val2,.....valn)
#obj.methodname()
    
    
#Example of object method :-
class School:
    sname = "SHA"
    loc = "Gorakhpur"
    principal = "Shaurya"
    timing = "9:00am to 4:30pm"
    def __init__(self, name, sid, age, bg):
        self.name = name
        self.sid = sid
        self.age = age
        self.bg = bg
    def display(self):
        print(self.name, self.sid, self.age, self.bg, self.sname, self.loc, self.principal, self.timing)
    def ch_age(self, new):
        self.age = new
st1 = School("Akanksha", 16, 24, "B+")
st1.display() #Output :- Akanksha 16 24 B+ SHA Gorakhpur Shaurya 9:00am to 4:30pm
st1.ch_age(25)
st1.display() #Output :- Akanksha 16 25 B+ SHA Gorakhpur Shaurya 9:00am to 4:30pm

#Prog to change employee because old employee is fired and new employee is hired in the company :-
class Company:
    cname = "Capgemini"
    loc = "Bangalore"
    ceo = "Alavya"
    def __init__(self, ename, eid, age, bg):
        self.ename = ename
        self.eid = eid
        self.age = age
        self.bg = bg
    def display(self):
        print(self.ename, self.eid, self.age, self.bg, self.cname, self.loc, self.ceo)
    def ch_ename(self, new):
        self.ename = new
    def ch_age(self, new):
        self.age = new
emp1 = Company("Shaurya", 23, 20, "AB+")
emp1.display() #Output :- Shaurya 23 20 AB+ Capgemini Bangalore Alavya
emp1.ch_ename("Akanksha")
emp1.display() #Output :- Akanksha 23 20 AB+ Capgemini Bangalore Alavya
emp1.ch_age(24)
emp1.display() #Output :- Akanksha 23 24 AB+ Capgemini Bangalore Alavya

#2. Class Method :- It is used to access and modify the class member.
#We need to use 'cls' as an argument to store the address of the class members. And it is compulsory to use @classmethod
#Syntax for class method :-
#class Cname:
    #Block of code
    #@classmethod                  #To access the class member
    #def mname(cls,args):          #To access the class member
        #statement block           #To access the class member
        #@classmethod               #To modify the class member
        #def mname(cls,new):        #To modify the class member
            #cls.var = new          #To modify the class member
#obj = Cname(val)
#Cname.mname(val)
        
#Class method example :-
class School:
    sname = "ABC"
    loc = "Paris"
    principal = "Alavya"
    timing = "8:00am to 1:00pm"
    @classmethod
    def display(cls):
        print(cls.sname, cls.loc, cls.principal, cls.timing)
    @classmethod
    def ch_timing(cls, new, change):
        cls.timing = new
        cls.loc = change
st1 = School()
School.display() #Output :- ABC Paris Alavya 8:00am to 1:00pm
School.ch_timing("8:30am to 1:30pm", "London")
School.display() #Output :- ABC London Alavya 8:30am to 1:30pm

#Class method example for company :-
class Company:
    cname = "Google"
    loc = "California"
    ceo = "Sundar Pichai"
    @classmethod
    def display(cls):
        print(cls.cname, cls.loc, cls.ceo)
    @classmethod
    def ch_ceo(cls, new):
        cls.ceo = new
emp1 = Company()
Company.display() #Output :- Google California Sundar Pichai
Company.ch_ceo("Shaurya")
Company.display() #Output :- Google California Shaurya

#Bank example for class method :-
class Bank:
    bname = "HDFC"
    loc = "Mumbai"
    manager = "Shaurya"
    @classmethod
    def display(cls):
        print(cls.bname, cls.loc, cls.manager)
    @classmethod
    def ch_manager(cls, new):
        cls.manager = new
cus1 = Bank()
Bank.display() #Output :- HDFC Mumbai Shaurya
Bank.ch_manager("Akanksha")
Bank.display() #Output :- HDFC Mumbai Akanksha

#Bank example for object method :-
class Bank:
    bname = "HDFC"
    loc = "Mumbai"
    manager = "Shaurya"
    def display(self):
        print(self.bname, self.loc, self.manager)
    def ch_manager(self, new):
        self.manager = new
cus1 = Bank()
cus1.display() #Output :- HDFC Mumbai Shaurya
cus1.ch_manager("Akanksha")
cus1.display() #Output :- HDFC Mumbai Akanksha

#Bank example for both class method and object method :-
class Bank:
    bname = "HDFC"
    loc = "Mumbai"
    manager = "Shaurya"
    def display(self):
        print(self.bname, self.loc, self.manager)
    def ch_manager(self, new):
        self.manager = new
    @classmethod
    def display(cls):
        print(cls.bname, cls.loc, cls.manager)
    @classmethod
    def ch_loc(cls, new):
        cls.loc = new
cus1 = Bank()
cus1.display() #Output :- HDFC Mumbai Shaurya
cus1.ch_manager("Akanksha")
cus1.display() #Output :- HDFC Mumbai Akanksha
cus1.ch_loc("Delhi")
cus1.display() #Output :- HDFC Delhi Akanksha


#Static Method :- It is neither belongs to class member nor belongs to object address but it will act as a supportive method for both class and objects.
#We use @staticmethod as decorator.
#Syntax for static method :-
#class Cname:
    #Block of code
    #@staticmethod
    #def mname(args):
        #statement block
#obj = Cname()

#Static method example:- 
class Boring:
    name = "Rehman"
    role = "Student"
    @staticmethod
    def nonsense(a,b):
        print(a+b)
st1 = Boring()
Boring.nonsense(10,20)
st1.nonsense(30,40)


#Prog
class Demo:
    @staticmethod
    def add(a,b):
        print(a+b)
Demo.add(10,20)

#Why is this static method ?
#Because it does not use object members.
#Because it does not use class members.
#Because it works independently.
#--Static method is a normal helper function inside a class--



#Pillars Of OOPS:- 
#1. Inheritance
#2. Encapsulation
#3. Polymorphism
#4. Abstraction

class A:
    def __init__(self):
        print("Hi")
    def __init__(self):
        print("Hello")
a = A()
#Output will be Hello

class B:
    def display(self):
        print("Hi")
    def display(self, a):
        print(a)
b = B()
b.display(10)



#Inheritance :- It is a process of inheriting or invoking the properties or attributes of parent class into child class.
#Syntax for inheritance :-
#class name(Parent class):
    #attribute and method of parent class.
#class name1(childclass):

#Code:- 
class Animal:      #Parent class or Super class or base class
    a = "Snake"    
    b = "Rabbit"
class Birds(Animal): #Child class or Derived class
    c = "kiwi"
    d = "Peacock"
b1 = Birds()
print(b1.a, b1.b, b1.c, b1.d)

#Create one inheritance class name will be A (Parent class) and child class will be B. 
#In class A there is a show method which print hello in class B there is a method name display which print hello world.
class A:      
    def show(self):   
        print("Hello")
class B(A): 
    def display(self):
        print("Hello World")
b1 = B()
b1.show()
b1.display()
#if func is return rather than print then we have to use print then call else just do like previous one.

#Types of Inheritance:- 
#1. Single level Inheritance
#2. Multi level Inheritance
#3. Multiple Inheritance
#4. Hierarichal Inheritance
#5. Hybrid Inheritance

#SINGLE LEVEL INHERITANCE:- 
#Flow Dig:-
#class A: #Parent class
#         .
#         .
#         .
#         .
#         .
#         .
#class B(A) #Child class

#In single level inheritance there aways one parent class and one child class is present.
#In single level inheritance the one child class can able to inherit all the properties , attributes and methods of the parent class.
#Syntax for single level inheritance :-
# class Parent:
    #Block of code(Attributes and methods of parent class)
# class Child:
    #Block of code(Attributes and methods of child class)
    
#Create a parent class Employee and attributes are emp name and salary.
#Create a child class Developer and attributes are prog lang and project.
#Diaplay method which will print whole detail emp name salary lang and project.

class Employee:
    emp_name = "Shaurya"
    salary = '100000'
class Developer(Employee):
    prog_lang = "Python"
    project = "ISL"
    def display(self):
        print(self.emp_name, self.salary, self.prog_lang, self.project)
shau = Developer()
shau.display()

#MULTI LEVEL INHERITANCE:-
#Flow Dig:-
#class A: # Parent class
#         .
#         .
#         .
#         .
#         .
#         .
#class B(A) #Child class but Parent class for class C
#         .
#         .
#         .
#         .
#         .
#         .
#class C(B) #Child class but Parent class for class D
#         .
#         .
#         .
#         .
#         .
#         .
#class D(C) #Child class 
#         .
#         .
#         .
#         .
#         .
#         .
#It is a phenomenon or driving property from parent class or from one class to another class by considering more than one level.
#In this case the last derived class will having all the properties from its parent class.
#It can easily access all the attributes of all the parent class.
#Syntax for multi level inheritance :-
# class C1:
    #Block of code(Attributes and methods of class C1)
# class C2(C1):
    #Block of code(Attributes and methods of class C2)
# class C3(C2):
    #Block of code(Attributes and methods of class C3)
#         .
#         .
#         .
#         .
#         .
#         .
#       n number of classes

#Create a class Bank wuth attribute branch name , manager name and constructor have all these two attributes
#Create a class ATM(Bank) having constructor with having print branch name , manager name , acc no., IFSC code.
#Create a class ATM2(ATM) having constructor with having print acc no, IFSC code , branch name and manager name.

class Bank:
    def __init__(self):
        self.branch_name = "GORAKHPUR"
        self.manager_name = "Shaurya"
        
class ATM(Bank):
    def __init__(self):
        super().__init__()
        self.acc_no = "1234567890"
        self.IFSC_code = "HDFC0001234"
class ATM2(ATM):
    def __init__(self):
        super().__init__()
        print(self.acc_no, self.IFSC_code, self.branch_name, self.manager_name)
a = ATM2()

#Constructor Chaining:-
#It is a process of calling or invoking the parent class constructor inside child class constructor.
#In constructor chaining we have to follow the syntax :- super().__init__(args)
#We can call the constructor or chain with class name also eg:- class_name__init__(args)

#Method Chaining:-
#It is the process of calling or invoking parent class method inside the child class method.
#The syntax for method chaining is :- super().method_name(args)
#Another syntax for method chaining is :- class_name.method_name(args)  #class name is parent class name here.

#Create a multilevel inheritance class A (Parent class) and class B (Child class) and class C (Child class of class B).
#All have method with same name show.
#Print hello in first then world in second and then hello world in third class by using method chaining.
class A:
    def show(self):
        print("Hello")
class B(A):
    def show(self):
        super().show()
        print("World")
class C(B):
    def show(self):
        super().show()
        print("Hello World")
a = C()
a.show()


class A:
    def show(self):
        print("Hello")
class B(A):
    def show(self):
        A.show(self)
        print("World")
class C(B):
    def show(self):
        B.show(self)
        print("Hello World")
a = C()
a.show()

#MULTIPLE INHERITANCE:- 
#It is a phenomenon of deriving the properties from multiple parent class into a single child class.
#Flow dig:-
#class A: #Parent class 1
#         .
#         .
#         .
#class B: #Parent class 2
#         .
#         .
#         .
#class C(B, A): #Child class
#Syntax for multiple inheritance :-
# class C1:
    #Block of code(Attributes and methods of class C1)
# class C2:
    #Block of code(Attributes and methods of class C2)
# class C3(C1, C2):     
    #Block of code(Attributes and methods of class C3)

#Create two parent class A with method show that prints Hello from A
#class B with method display that prints Hello from B
#Create a child class C that inherit A and B.

class A:
    def show(self):
        print("Hello from A")
class B:
    def display(self):
        print("Hello from B")
class C(A, B):
    pass
shau = C()
shau.show()
shau.display()


#HIERARCHAL INHERITANCE:-
#Syntax:- 
#class A: #Parent class
#         .
#         .
#         .
#class B(A): #Child class 1
#         .
#         .
#         .
#class C(A): #Child class 2
#         .
#         .
#         .
#It is the phenomenon of deriving the properties and attributes and methods from a single parent class into multiple child class.
#Create a parent class Vehicle with attributes v_name and v_number.
#Create two child class Car and Bike.
#Create an object method for car and bike where in car class declare fuel type as an attribute inside that print v_name and number and fuel type.
#Create an object method for bike class where in bike class declare fuel type as an attribute inside that print v_name and number and fuel type.

class Vehicle:
    v_name = "BMW"
    v_number = "ABC123"
class Car(Vehicle):
    fuel = "Disel"
    def display(self):
        print(self.v_name, self.v_number, self.fuel)
class Bike(Vehicle):
    fuel = "Petrol"
    cc = "2000"
    def show(self):
        print(self.v_name, self.v_number, self.fuel, self.cc)
shau = Car() 
shau1 = Bike()
shau.display()
shau1.show()



#HYBRID INHERITANCE:-
#Combination of more than one type of inheritance is called as hybrid inheritance.




#Polymorphism:-
#Poly = Many and Morph = Forms
#It is the phenomenon of making the same operator or method to perform two or more oprations.
#Addition operator is example of polymorphism because it can perform addition of two numbers as well as concatenation of two strings.
#How to achieve polymorphism in python :-
#1. Operator Overloading
#2. Method Overloading
#3. Method Overriding

#OPERATOR OVERLOADING:-
#Example:- 
class A:
    def __init__ (self,a):
        self.a = a
    def __add__(self, others):
        return self.a + others.a
obj = A(10)
obj1 = A(20)
print(obj + obj1) #Output :- 30


#Second Example:- 
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, shaurya, alavya, aman, vashu):
        return self.value + shaurya.value + alavya.value + aman.value + vashu.value
num1 = Number(10)
num2 = Number(20)
num3 = Number(30)
num4 = Number(40)
num5 = Number(50)
print(num1.__add__(num2, num3, num4, num5)) #Output :- 150


#Example Third:- 
class A:
    def __init__ (self,a):
        self.a = a
    def __add__(self, others):
        print(self.a + others.a)
        print(self.a - others.a)
        print(self.a * others.a)
        print(self.a / others.a)
obj = A(10)
obj1 = A(20)
obj + obj1


#METHOD OVERRIDING:-
#1. When we use same func name for two or more operation then the first func address will get override by the address of next func.
#If you want to access a particular method we have to make use of monkey patching concept.
class A:
    def display(self):
        print("a python")
    def display(self):
        print("Hello")
    def display(self):
        print("TATA")
obj = A()
obj.display() #Output :- TATA
#If I need to print Hello only rather than TATA and a python then we use mokey patching :-
class A:
    def display(self):
        print("a python")
    a = display
    def display(self):
        print("Hello")
    b = display
    def display(self):
        print("TATA")
    c = display
obj = A()
obj.display()
obj.a()
obj.b()
obj.c()
#Moneky patching is storing previous method address to a variable and accessing that method using the variable, previous code is example of moneky patching.

#METHOD OVERLOADING:-
#It is the process of using same method name to perform two or more different operation.
#In python we are going to perform method overloading it will act as a method overriding but in python we can achieve 
#method overloading with the help of default parameter.
#Example:- 
# class A:
#     def show(self, a):
#         print(self.a)
#     def show(self, a, b):
#         print(self.a + self.b)
#     def show(self, a, b, c):
#         print(self.a + self.b + self.c)
# obj = A()
# obj.show(10,20)

# #Example:- 
# class A:
#     def display(self, *a):
#         print(sum(a))
# obj = A()
# obj.display(10)
# obj.display(10,20)
# obj.display(10,100,144,66,78)


#ENCAPSULATION:-
#It is the concept of oops that means wrapping the data , attributes , variables, methods inside a function or a class
#That operator on that data into a single unit.
#And restricting the direct access to the components.
#Encaapsulation means it is the process of hiding the details of an object and allowing the access only through control methods.
#It is the combination of data hiding and abstraction.

#How to achieve encapsulation by access specifier :-
#1. Public Access Specifier
#2. Private Access Specifier(__ :- double underscore used for private access specifier)
#3. Protected Access Specifier(_ :- single underscore used for protected access specifier)
#By default all the attributes are public access specifiers.

#Public Access Specifier:-
#Public members can be accessed outside the class and also in derived class.
#The normal members that we are created in a normal class act as public members.
#There is no need of underscore for any kind of initialization for public access specifier.
#Example for public access specifier :-
class A:
    a = "Shaurya"
    def show(self):
        print(self.a)
obj = A()
print(obj.a)

#Make a parent class A put some attributes then make a child class B try to access class A properties inside the child class
class A:
    a = "Shaurya"
class B(A):
    pass
shau = B()
print(shau.a)

#Protected Access Specifier:-
#In protected access specifier variables or methods that is intended to be access within the class and its child class.
#In python protected members are represented by single underscore.
#We have to mention single underscore before the attributes name or the methods name.
#Example:-
class A:
    def __init__(self):
        self._name = "Shaurya"
        self._salary = 10000000000
class B(A):
    def show(self):
        print(self._name)
        print(self._salary)
shh = B()
print(shh._name)
print(shh._salary)


#Private Access Specifier:- 
#These are the members of the class which will provide security to the members present inside the class.
#To make private members it is compoulsory to make use of double underscore (__).
#Private members can not be accessed in the derived class but we can still access by using Name Mangling.

#Example:-
# class A:
#     __salary = 50000000000000000000000000000000
#     __company = "Google"
# class B(A):
#     def show(self):
#         print(self.__salary)
#         print(self.__company)
# shau = B()
# print(shau.__salary)
#Output :- ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 9, in <module>
# AttributeError: 'B' object has no attribute '__salary'. Did you mean: '_A__salary'?

# === Code Exited With Errors ===

class A:
    __salary = 50000000000000000000000000000000
    __company = "Google"
class B(A):
    def show(self):
        print(self.__salary)
        print(self.__comapny)
shau = B()
print(shau._A__salary)
#Output :- 50000000000000000000000000000000
#Syntax for accessing :- 
#obj_name._class_name__attribute/Methods
#This syntax is called Name Mangling.

#Example for accessing method:- 
class A:
    __salary = 500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    __company = "Google"
class B(A):
    def __show(self):
        print("Hello")
shau = B()
shau._B__show()
print(shau._A__salary)

#Abstraction :- 
#1. It is the process of hiding the implementation details and showing the essential features of an object to the user.
#We will try to hide the actual implementation and only provide the features.
#To achieve abstraction we have to make an abstract class for that we have to import abc module like this:- from abc import ABC, abstractmethod.
#There are three main component of abstraction:-
#Abstract Class
#Abstract Method
#Concrete CLass





#ABSTRACT METHOD:- 
#It is the method which consist of function declaration but not function implementation.
#To make abstract method we have to use decorator @abstractmethod.
#Syntax:- 
#@abstractmethod
#def func_name(self):
#    pass



#ABSTRACT CLASS:-
#It is the class in which we are trying to inherit abc, and it also consist of atleast one abstract method.
#It is not possible to create an object using abstract class.
#Syntax:- 
#from abc import ABC, abstractmethod
#class <ClassName>(ABC):
#     Attributes and methods



#Concrete Class:-
#It is the class which doesn't consist of any abstract method, we can call it as concrete class.
#It is possible to create an object using concrete class or for the concrete class.

#Example:-
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass
class Car(Vehicle):
    def engine(self):
        print("Start the engine")
obj = Car()
obj.engine()

#Second thing if we write fuel instead of engine:-
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def engine(self):
#         pass
# class Car(Vehicle):
#     def fuel(self):
#         print("Start the engine")
# obj = Car()
# obj.engine()
# #Error :- Traceback (most recent call last):
#   File "c:\Users\hp\OneDrive\Desktop\PYTHON\oops.py", line 994, in <module>
#     obj = Car()
# TypeError: Can't instantiate abstract class Car with abstract method engine


#Example second:-
# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(Payment):
#     def pay(self):
#         print("Pay using UPI")
# class CreditCard(Payment):
#     def pay(self):
#         print("Pay using Credit Card")
# class Crypto(Payment):
#     def otp(self):
#         print("Pay using Crypto")
# a = Crypto()
# a.otp()

#Ques1:- Create an abstract class shape with an abstract method area.
#Create a child class: Rectangle , square.
#Implement the area method in Rectangle and square.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        l = 10
        b = 20
        a = l * b 
        print("Area of Rectangle:-", a)
class Square(Shape):
    def area(self):
        a = 10
        b = a*a 
        print("Area of Square:-", b)
shau = Rectangle()
shau.area()

shau1 = Square()
shau1.area()