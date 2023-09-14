n = float(input("Nhap n: "))
s = 0
t = n
while(t != 0):
    dv = t % 10
    s = s + dv
    t = int(t/10)
print("S = ", s)