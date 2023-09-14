import math
def TinhGiaiThua(n):
    result = 1
    for i in range(n):
        result*=(i+1)
    return result
x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
result = 0
for i in range(n):
    result+= (math.pow(x,i+1))/TinhGiaiThua(i+1)
print(result)
