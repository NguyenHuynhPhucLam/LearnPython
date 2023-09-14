import math

def TinhSin(x,n):
    result = x
    for i in range(n):
        result = math.sin(result)
    return result
x = int(input())
n = int(input())
result = 0
for i in range(n):
    result+=TinhSin(x,i+1)
print(result)
