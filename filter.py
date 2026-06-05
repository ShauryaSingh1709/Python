#Filter all the odd number
a = [2,4,3,5,6,7,8]
b = filter(lambda x: x%2 != 0, a)
print(list(b))
