from math import sqrt


x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
t = 1
i = 1 
while(i <= n):
    t = t * x
    s = sqrt(t + s) 
    i = i + 1 
print("s =", s)
