import math

s = 0
e = 1
i = 1

while(e >= math.pow(10,-6)):
    e = 1 / i
    s = s + e
    i = i + 2
print(s)
