def tinh_tong(x, n):
    tong = 0.0
    dau = 1  
    
    for i in range(1, n + 1):
        tong += dau * (x ** i)
        dau *= -1  
        
    return tong

x = float(input("x: "))
n = int(input("n: "))
ket_qua = tinh_tong(x, n)
print(f"S({x}, {n}) = {ket_qua}")

