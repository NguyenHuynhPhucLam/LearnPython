import math

n = int(input("Nhap n (n >= 1): "))
while n < 1:
    print("n > 1, nhap lai!")
    n = int(input("Nhap n (n >= 1): "))

S = 0.0
for i in range(1, n + 1):
    S = math.sqrt(i + S)

print("Tong S =", S)

