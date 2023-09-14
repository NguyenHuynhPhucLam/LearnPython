import math

x1, y1 = map(float, input("Nhap (x1 y1): ").split())
x2, y2 = map(float, input("Nhap (x2 y2): ").split())
x3, y3 = map(float, input("Nhap (x3 y3): ").split())

ab_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
bc_distance = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
ca_distance = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

perimeter = ab_distance + bc_distance + ca_distance

print(f"Chu vi cua tam giac ABC la: {perimeter}")
