import math

n = int(input("Nhap n duong: "))

if n > 0 and math.isqrt(n)**2 == n:
    print(f"{n} la so chinh phuong.")
else:
    print(f"{n} khong phai la so chinh phuong.")

