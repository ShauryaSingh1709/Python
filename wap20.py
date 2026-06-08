#Example 1 :- Simple Question Create a parent class Animal with a method eat(). Create a child class Dog that inherits from Animal and adds a method bark() in the child class. Create an object of Dog and call both methods.
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
obj1 = Dog()
obj1.eat()
obj1.bark()

#Example 2 : Employee → Developer : Problem Statement
# Create a parent class Employee.
# Initialize:
# employee name
# salary
# Create child class Developer.
# Add:
# programming language
# Display all details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Developer(Employee):
    def __init__(self, name, salary, prog_lang):
        super().__init__(name, salary)
        self.prog_lang = prog_lang
    def display(self):
        print(self.name, self.salary, self.prog_lang)
obj1 = Developer("Shaurya", 100000, "Python")
obj1.display()


#Example 3 :- Create a Resume Builder using Multilevel Inheritance.
# Create a class Resume10th to store personal details and 10th academic details.
# Create a class Resume12th that inherits from Resume10th and stores 12th academic details.
# Create a class ResumeDegree that inherits from Resume12th and stores degree academic details.
# Use constructor chaining to initialize all data.
# Use methods to display the resume details at each level.
# Create objects for a 12th-pass student and a degree student and display their resumes.

class Resume10th:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
class Resume12th(Resume10th):
    def __init__(self, name, age, address, school):
        super().__init__(name, age, address)
        self.school = school
class ResumeDegree(Resume12th):
    def __init__(self, name, age, address, school, degree):
        super().__init__(name, age, address, school)
        self.degree = degree
    def display(self):
        print(self.name, self.age, self.address, self.school, self.degree)
obj1 = ResumeDegree("Shaurya", 20, "Bangalore", "Sacred Heart Academy", "B.Tech")
obj1.display()

#Example 4:- Create an Employee Management System using Hierarchical Inheritance.
# Create a parent class Employee with:
# name
# email
# Create two child classes:
# Developer (programming language, experience)
# Tester (testing tool, experience)
# Requirements
# Use constructor chaining with super().
# Create two methods in the parent class:
# display_basic_details()
# display_contact_details()
# Extend these methods in both child classes by adding their own details.
# Use method chaining to display the complete information of a Developer and a Tester.

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email    
class Developer(Employee):
    def __init__(self, name, email, prog_lang, exp):
        super().__init__(name, email)
        self.prog_lang = prog_lang
        self.exp = exp
    def display(self):
        print(self.name, self.email, self.prog_lang, self.exp)
class Tester(Employee):
    def __init__(self, name, email, test_tool, exp):
        super().__init__(name, email)
        self.test_tool = test_tool
        self.exp = exp
    def display(self):
        print(self.name, self.email, self.test_tool, self.exp)
obj1 = Developer("Shaurya", "shaurya17092006@gmail.com", "Python", 1)
obj2 = Tester("Shaurya", "shaurya123@gmail.com", "Java", 1)
obj1.display()
obj2.display()


#Example 5:- Create a Calculator application using Multiple Inheritance.
# Addition
# Create a class Addition with a method to add two numbers.
# Subtraction
# Create a class Subtraction with a method to subtract two numbers.
# Multiplication
# Create a class Multiplication with a method to multiply two numbers.
# Calculator
# Create a class Calculator that inherits from:
# Addition
# Subtraction
# Multiplication
# Create an object of Calculator and perform all three operations.

class Addition:
    def add(self, a, b):
        return a + b
class Subtraction:
    def sub(self, a, b):
        return a - b
class Multiplication:
    def mul(self, a, b):
        return a * b
class Calculator(Addition, Subtraction, Multiplication):
    pass
obj1 = Calculator()
print(obj1.add(10, 20))
print(obj1.sub(10, 20))
print(obj1.mul(10, 20))





















































































