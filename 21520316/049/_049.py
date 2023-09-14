n = int(input())
array = []
for i in range(int(n)):
    if(n%(i+1)==0):
        array.append(i+1)
print(array)
