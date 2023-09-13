from math import sqrt

n = float(input("Nhap n: "))
s = 0
i = 1
while(i <= n):
    s = s + sqrt(1 + (1 / (i ** 2)) + (1 / ((i + 1) ** 2)))
    i = i + 1
print("s =", s)

