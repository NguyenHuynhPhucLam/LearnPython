import math
n = int(input())
at = 2
i = 2
ahh = 0
while(i<=n):
    ahh = (math.pow(at,2) + 2) / (2 * at)
    i=i+1
    at = ahh
print(ahh)    
