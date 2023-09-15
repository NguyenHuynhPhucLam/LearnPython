
import math

n = int(input())
result = 0
for i in range(n):
    result+=math.sqrt(result+i+1)
print(result)