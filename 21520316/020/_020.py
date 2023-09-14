def power(x, n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return x * power(x, n - 1)
    else:
        half = power(x, n // 2)
        return half * half

x = float(input("Nhap x: "))
n = 14  

result = power(x, n)
print(f"{x}^{n} = {result}")

