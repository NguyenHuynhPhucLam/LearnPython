x = int(input())

if(x<2):
    print("khong phai snt")
elif(x==2):
    print("x la so nguyen to")
elif(x%2==0):
    print("x khong la snt")
else:
    for i in range(int(x/2)):
        if(i+1>2 and n%(i+1) == 0):
            print("x khong snt")
    print("x la snt")  
