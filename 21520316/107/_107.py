from math import pi

x = float(input("Nhap x: "))
xx = (x * pi) / 180
s = 1
t = 1
m = 1
dau = -1
e = 1
i = 2
while(e >= (10 ** (-6))):
    t = t * xx ** 2
    m = m * (i - 1) * i
    e = t / m
    s = s + dau * e
    dau = dau * (-1)
    i = i + 2
print("s =", s)
