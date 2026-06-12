# Generator :- It is a function which is used to produce values on demand using 'yield' keyword.
# Generators are memory efficient as they produce values lazily (one at a time).
# They return an iterator object that can be used in loops or with next().

# Syntax:-
# def <generator_name>(parameters):
#     yield value

# Example 1: Simple Generator
def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Example 2: Generator with loop - Countdown
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1

# Example 3: Fibonacci Generator
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))  # Output: [0, 1, 1, 2, 3, 5, 8]

# Example 4: Generator Expression (like list comprehension but lazy)
squares = (x*x for x in range(10))
print(next(squares))  # Output: 0
print(list(squares))  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 5: Even Numbers Generator
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(list(even_numbers(10)))  # Output: [0, 2, 4, 6, 8]

# Example 6: Generator for reading large files (memory efficient)
def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

# Example 7: Infinite Sequence Generator
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

# Use with caution - infinite sequence
# counter = infinite_counter()
# print(next(counter))  # 0
# print(next(counter))  # 1