t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    print((b-a)//10 if (b-a)%10==0 else (b-a)//10+1 )