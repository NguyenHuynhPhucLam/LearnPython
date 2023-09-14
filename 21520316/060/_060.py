def tinh_tich_cac_chu_so(n):
    str_n = str(n)
    
    tich = 1
    
    for digit in str_n:
        tich *= int(digit)
    
    return tich

n = int(input("Nhap n duong: "))
ket_qua = tinh_tich_cac_chu_so(n)
print(f"Tich cac chu so cua {n} la: {ket_qua}")

