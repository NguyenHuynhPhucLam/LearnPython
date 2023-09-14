from math import sqrt

x1 = float(input("Nhap x1: "))
y1 = float(input("Nhap y1: "))
x2 = float(input("Nhap x2: "))
y2 = float(input("Nhap y2: "))
x3 = float(input("Nhap x3: "))
y3 = float(input("Nhap y3: "))

a = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
b = sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
c = sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))

p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))


print("Dien tich tam giac nay =", s)
