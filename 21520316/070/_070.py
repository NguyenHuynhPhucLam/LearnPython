def tinh_tong(x, n):
    tong = 0.0
    for i in range(n + 1):
        tong += x**(2*i)
    return tong

x = float(input("x: "))
n = int(input("n: "))
ket_qua = tinh_tong(x, n)
print(f"S({x}, {n}) = {ket_qua}")

