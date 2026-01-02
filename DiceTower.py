n=int(input())
ls=[int(x) for x in input().split()]
for x in ls:
    if x>21:
        print("YES" if 8<=42-x<=13 else "NO")
    else:
        print("YES" if 1 <= 21 - x <= 6 else "NO")
        