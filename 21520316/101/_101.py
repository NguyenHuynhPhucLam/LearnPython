from math import pow

s = 0
e = 1
i = 1
while (e>=pow(10,-6)):
    e = 1/i
    s = s + e
    i = i + 1

print("S(n) =", s)
