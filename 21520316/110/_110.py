from math import pow

s = 3
dau = 1
e = 3
i = 2
while (e >= pow(10, -4)):
    e = 4 / (i * (i + 1)) 
    s = s + dau*e
    dau = - dau
    i = i + 2
    
print("pi = ", s)

