def tinh_tong(n):
    tong = 0.0
    for i in range(1, n + 1):
        tong += i * (i + 1)
    return tong

n = int(input("Nhap gia tri n: "))
ket_qua = tinh_tong(n)
print(f"S({n}) = {ket_qua}")
