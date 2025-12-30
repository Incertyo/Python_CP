t=int(input())
for i in range(t):
    x,y,n=map(int,input().split())
    rem= n%x
    if rem<y:
        n=n-(x-y+rem)
    elif rem>y:
        n=n-rem+y
    print(n)
