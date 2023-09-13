x = float(input("Nhap x: "))
n = float(input("Nhap n: "))

t = x
i = 1

while(i <= n):
    t = t * (x+i)
    i = i + 1

print("S = ", t)