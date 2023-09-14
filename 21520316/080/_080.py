def tinh_tong(x, n):
    tong = 0.0
    mau_so = 1.0
    for i in range(n + 1):
        mau_so *= x + i
        tong += 1 / mau_so
    return tong

x = float(input("x: "))
n = int(input("n: "))
ket_qua = tinh_tong(x, n)
print(f"S({x}, {n}) = {ket_qua}")

