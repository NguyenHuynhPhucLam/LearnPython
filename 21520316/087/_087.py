x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = x
t = x
i = 3
dau = -1
while(i <= (2 * n + 1)):
    t = t * x * x
    s = s + dau * t
    i = i + 2
    dau = dau * (-1)
print("s =", s)

