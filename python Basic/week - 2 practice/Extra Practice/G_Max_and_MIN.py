from functools import reduce
n = input()
l = list(map(int,input().split()))
mn = lambda x,y: x if x<y  else y
mx = lambda x,y: x if x>y  else y
ans1 = reduce(mn,l)
ans2 = reduce(mx,l)
print(ans1,ans2)