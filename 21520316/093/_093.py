import math

n = float(input("Nhap n: "))

s = 0
i = 1

while(i <= n):
    s = math.sqrt(2 + s)
    i = i + 1
print(s)