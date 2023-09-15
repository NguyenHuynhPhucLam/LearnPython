import math
x = int(input())
result = 1
for i in range(x):
    result*=(1+1/(math.pow(i+1,2)))
print(result)