x = int(input("Nhap x: "))
y = int(input("Nhap y: "))

n = x
print("Nam nhuan trong doan [", x, ",", y, "]: ")
while n <= y:
	dk1 = (n % 4 == 0) and (n % 100 != 0)
	dk2 = bool(n % 400 == 0)
	if dk1 or dk2:
		print(n)
	n += 1
