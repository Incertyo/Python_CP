n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    if a%b==0:
        print(0)
    else:
        print(b-(a%b))
