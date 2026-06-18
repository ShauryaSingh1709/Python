#1.	Write a Python program to create a file and write some text into it.
shau = open('Shaurya.txt', 'w')
shau.write('This is Shaurya')
shau.close()

#2.	Write a Python program to read the contents of a file and display them on the screen.
shau = open('Shaurya.txt', 'r')
print(shau.read())
shau.close()

#3.	Write a Python program to append new text to an existing file.
shau = open('Shaurya.txt', 'a')
shau.write('\nI am Python Developer')
shau.close()

#4.	Write a Python program to count the number of lines, words, and characters in a text file.
with open("Shaurya.txt", "r") as file:
    content = file.read()
num_lines = len(content.splitlines())
num_words = len(content.split())
num_chars = len(content)
print(f"Lines: {num_lines}")
print(f"Words: {num_words}")
print(f"Characters: {num_chars}")

#5.	Write a Python program to copy the contents of one file to another file.
shau = open('Shaurya.txt', 'r')
shau1 = open('Shaurya1.txt', 'w')
shau1.write(shau.read())
shau.close()
shau1.close()

#6.	Write a Python program to count the number of vowels, consonants, digits, and special characters in a file.
with open("Shaurya.txt", "r") as file:
    content = file.read()
vowels = 0
consonants = 0
digits = 0
special_chars = 0
for char in content:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special characters: {special_chars}")

#7.	Write a Python program to search for a specific word in a file and count its occurrences.
with open("Shaurya.txt", "r") as file:
    content = file.read()
word = input("Enter the word to search: ")
count = content.count(word)
print(f"The word '{word}' appears {count} times in the file.")


#8.	Write a Python program to replace a particular word in a file with another word.
with open("Shaurya.txt", "r") as file:
    content = file.read()
a = input("Enter the word to replace: ")
b = input("Enter the word to replace with: ")
modified = content.replace(a, b)
with open("Shaurya.txt", "w") as file:
    file.write(modified)
print("Word replaced successfully.")

#9.	Write a Python program to read a file line by line and store each line in a list.
with open("Shaurya.txt", "r") as file:
    lines = file.readlines()
print(lines)


#10.	Write a Python program to store student details (Roll No., Name, Marks) in a file and then display them.
with open("student_details.txt", "w") as file:
    roll_no = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    file.write(f"Roll No: {roll_no}\nName: {name}\nMarks: {marks}\n")

with open("student_details.txt", "r") as file:
    print(file.read())