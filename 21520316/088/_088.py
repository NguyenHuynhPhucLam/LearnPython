n = float(input("Nhap n: "))

s = 0 
m = 0 
i = 1
dau = 1

while(i <= n):
    m = m + i
    s = s + dau / m
    i = i + 1
    dau = -1 * dau
print(s)