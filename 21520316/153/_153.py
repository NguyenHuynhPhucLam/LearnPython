n = float(input("Nhap n: "))

flag = 1
t = n

while(t > 1):
    du = t % 5
    if(du != 0):
        flag = 0
    t = int(t/5)

if(flag == 1):
    print("dung dang de bai cho")
else:
    print("khong la dang de bai cho")
