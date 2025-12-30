n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    side=0
    if a>b:
        side=max(a,b*2)
    else:
        side=max(a*2,b)
    print(side**2)