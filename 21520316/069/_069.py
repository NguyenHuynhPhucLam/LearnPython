import math
x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
result = 0
for i in range(n):
    result += math.pow(x,i+1)
print(result)
