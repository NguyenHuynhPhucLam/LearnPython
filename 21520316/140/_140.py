import math

a = float(input("Nhap a (khac 0): "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))

if a == 0:
    print("A khac khong de day la phuong trinh bac hai")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phuong trinh co hai nghiem phan biet:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print("Phuong trinh co mot nghiem kep:")
        print(f"x = {x}")
    else:
        print("Phuong trinh khong nghiem.")

