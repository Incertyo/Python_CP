n=int(input())
for i in range(n):
    a=int(input())
    ls=[]
    if a&(a-1)==0 and a>2:
        t=1
        print("YES")
        for i in range(a//2):
            ls.append((i+1)*2)
        for i in range(a//2-1):
            ls.append(ls[i]-1)
        ls.append((a//2-1)+ls[a//2-1])
        for i in range(a):
            print(ls[i],end=' ')
        print( )
    else:
        print("NO")