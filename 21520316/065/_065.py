def tim_chu_so_nho_nhat(n):
    str_n = str(n)
    
    chu_so_nho_nhat = int(str_n[0])
    
    for digit in str_n:
        chu_so = int(digit)
        if chu_so < chu_so_nho_nhat:
            chu_so_nho_nhat = chu_so
    
    return chu_so_nho_nhat

n = int(input("Nhap n duong: "))
ket_qua = tim_chu_so_nho_nhat(n)
print(f"Chu so nho nhat cua {n} la: {ket_qua}")

