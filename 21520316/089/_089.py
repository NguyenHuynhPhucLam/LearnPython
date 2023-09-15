
import math
def tinhSum(n):
    result = 0
    for i in range(n):
        result+= i+1
    return result
x = int(input())
n = int(input())
arr = []
result = 0
for i in range(n):
    arr.append(i+1)
    print(sum(arr))
    result+= ( math.pow(-x,i+1) / sum(arr))
print(result)
