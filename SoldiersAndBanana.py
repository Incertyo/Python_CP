k,w,n=map(int,input().split())
ans=(k*(n*(n+1))//2)-w
print(0 if ans<0 else ans)