t= int(input())
for i in range(t):
    n=int(input())
    ls=[int(i) for i in input().split()]
    c=0
    odd = even = 0
    for i in range(n):
        if ls[i] % 2 != i % 2:
            if ls[i] % 2 == 0:
                even+= 1
            else:
                odd += 1

    if odd == even:
        print(odd)
    else:
        print(-1)
