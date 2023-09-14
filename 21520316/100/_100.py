import math

n = int(input("Nhap n (n >= 1): "))
while n < 1:
    print("n >= 1")
    n = int(input("Nhap n (n >= 1): "))

S = 0.0
M = 1

for i in range(1, n + 1):
    M = M * i
    S = math.sqrt(M + S)

print("Tong la", S)

