def tinh_tong_uoc_so(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong

n = int(input("Nhap n duong: "))
ket_qua = tinh_tong_uoc_so(n)
print(f"Tong cac uoc so cua {n} la: {ket_qua}")

