import math

n = int(input())
at = -2
tt = 3
pp = 7
i=2
ahh=0
while(i<=n):
    tt = tt*3
    pp = pp*7
    ahh = 5*at + 2*tt - 6 * pp+12
    i=i+1
    at=ahh
print(ahh)
