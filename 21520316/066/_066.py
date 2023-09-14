n = int(input("Nhap n: "))

flag = 0
t = n

while(t!=0):
    dv = t % 10
    if(dv%2 == 0):
        flag = True
    t = t // 10
if(flag == 1):
    print(n,"ton tai chu so chan")
else: 
    print(n,"khong ton tai chu so chan")
