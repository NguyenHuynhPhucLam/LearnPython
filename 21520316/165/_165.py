n = int(input("Nhap n: "))

k = 0

while 2**k < n:
    k += 1

k -= 1

print({k})

