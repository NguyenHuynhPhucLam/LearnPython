import math

n = int(input())
result = 0
for i in range(n):
    result=(result+i+1) ** (1/(i+2))
print(result)