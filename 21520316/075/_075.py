import math

def tinh_tong(x, n):
    tong = 0.0
    for i in range(n + 1):
        tu_so = x**(2*i)
        mau_so = math.factorial(2*i)
        tong += tu_so / mau_so
    return tong

x = float(input("x: "))
n = int(input("n: "))
ket_qua = tinh_tong(x, n)
print(f"S({x}, {n}) = {ket_qua}")

