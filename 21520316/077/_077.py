n = float(input("Nhap n: "))
k = int(input("Nhap k: "))
s = 0
i = 1
while(i <= n):
    s = s + (i ** k)
    i = i + 1
print("s =", s)