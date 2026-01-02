n,k=map(int,input().split())
if k==1:
    print(n)
else:
   h= n.bit_length()-1
   print((1<<(h+1))-1)