#WAP to find sum of all number starting from 1 to 25 then 26 to 50 then 51 to 75.

sum = 0
for i in range(1, 26):
    sum += i
sum1 = 0
for i in range(26, 51):
    sum1 += i
sum2 = 0
for i in range(51, 76):
    sum2 += i
print(sum)
print(sum1)
print(sum2)