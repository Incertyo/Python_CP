ls=[int(x) for x in input().split()]
ls.sort()
print(ls[-1]-ls[-2],ls[-1]-ls[-3],ls[-1]-ls[-4])