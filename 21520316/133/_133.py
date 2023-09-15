x = float(input("Nhap x: "))
y = float(input("Nhap y: "))
z = float(input("Nhap z: "))

if(x+y>z and y+z>x and z+x>y):
    if(x==y and y==z):
        print("La tam giac deu")
    elif((x*x==y*y+z*z) or (y*y==x*x+z*z) or (z*z==x*x+y*y)):
        if((x==y) or (y==z) or (z==x)):
            print("La tam giac vuong can")
        else:
            print("La tam giac vuong")
    elif((x==y) or (y==z) or (z==x)):
        print("La tam giac can")
    else:
        print("La tam giac thuong")
else:
    print("Khong la tam giac")
