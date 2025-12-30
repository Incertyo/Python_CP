n= int(input())
ls=[int(x) for x in input().split()]
length=1
c=1
for i in range(1,n):
    if ls[i]>ls[i-1]:
        c+=1
    else:
        c=1
    length=max(length,c)
print(length)