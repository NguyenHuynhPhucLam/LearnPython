def Nhap():
    x = int(input("Nhap so nguyen n: "))
    while x < 1:
        print("Nhap sai, yeu cau nhap lai!")
        x = int(input("Nhap so nguyen n: "))
    return x

def Tinh(n):
    s = 0.0
    t = 0.0
    for i in range(1, n + 1):
        t += i
        s += 1.0 / t
    return s

n = Nhap()
ket_qua = Tinh(n)
print("Ket qua la:", ket_qua)

