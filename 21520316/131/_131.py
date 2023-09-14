from math import sqrt, pow

xA = float(input("Nhap xa: "))
yA = float(input("Nhap ya: "))
xB = float(input("Nhap xb: "))
yB = float(input("Nhap yb: "))
xC = float(input("Nhap xc: "))
yC = float(input("Nhap yc: "))
a = sqrt(pow(xB-xA, 2)+pow(yB-yA, 2))
b = sqrt(pow(xC-xB, 2)+pow(yC-yB, 2))
c = sqrt(pow(xA-xC, 2)+pow(yA-yC, 2))
if a + b > c and a + c > b and b + c > a:
    print("ABC la tam giac!")
else:
    print("ABC khong la tam giac!")
