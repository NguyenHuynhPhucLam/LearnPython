x = float(input("Nhap x: "))
y = float(input("Nhap y: "))
z = float(input("Nhap z: "))

if x >= 0 and y >= 0 and z >= 0:
    if x + y > z and x + z > y and y + z > x:
        print("Co ton tai tam giac vai do dai ba canh la x,z,z.")
    else:
         print("Khong ton tai tam giac vai do dai ba canh la x,z,z.")
else:
    print("So x, y, z phai khong am de tao thanh mot tam giac.")

