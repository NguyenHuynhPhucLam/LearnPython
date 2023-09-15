import math

a = int(input("Nhap a duong: "))
b = int(input("Nhap b duong: "))

uscln = math.gcd(a, b)

bcnn = (a * b) // uscln

print(f"BCNN cua {a} va {b} la {bcnn}.")

