from math import sqrt

n = int(input("Nhap n: "))

s = 0
i = 1
while(i<=n):
    s = s + 1/((i + 1)*sqrt(i) + sqrt(i + 1)*i)
    i = i + 1

print("S(",n,") =", s)
