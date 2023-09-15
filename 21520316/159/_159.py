n = int(input())
temp = n
minVal = 9 
count = 0
while(temp>0):
    if(temp%10<minVal):
        minVal = int(temp%10)
    temp = int(temp/10)
while(n>0):
    if(n%10 == minVal):
        count+=1
    n = int(n / 10)
print(count)
