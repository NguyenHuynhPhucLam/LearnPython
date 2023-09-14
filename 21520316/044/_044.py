import math

n = int(input())
result = 0
for i in range(n):
    result += 1/((i+1) * (i+2) * (i+3) * (i+4))
print(result)

