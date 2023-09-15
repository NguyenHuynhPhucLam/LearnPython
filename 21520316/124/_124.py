import math
n = int(input())
at = 2
bt = 1
i = 2
while(i<=n):
    ahh = at*at + 2*bt*bt
    bhh = 2*at*bt
    i=i+1
    at=ahh
    bt = bhh
print("a: ", ahh)
print("b: ",bhh)