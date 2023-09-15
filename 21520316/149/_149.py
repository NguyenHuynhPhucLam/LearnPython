a = int(input())
b = int(input())
m = abs(a)
n = abs(b)
while(m*n!=0):
    if(m>n):
        m = m - n
    else:
        n=n-m
ucln = m + n
print(ucln)
