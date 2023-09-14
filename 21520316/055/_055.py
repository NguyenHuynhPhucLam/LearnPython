def tinh_tich_uoc_so_le(n):
    tich = 1
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            tich *= i
    return tich

n = int(input("Nhap so nguyen duong n: "))
ket_qua = tinh_tich_uoc_so_le(n)
print(f"Tich cua tat ca cac uoc so le cua {n} la: {ket_qua}")

