n = int(input("Nhap n: "))
dt = abs(n)
while(dt >= 10):
    dt = int(dt / 10)
print("Chu so dau tien cua", n,"la:", dt)
