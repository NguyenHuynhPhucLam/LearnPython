n = int(input())
max = 0
while(n>0):
    if(max<n%10):
        max=n%10
    if(max==9):
        break
    n= int(n/10)
print(max)
