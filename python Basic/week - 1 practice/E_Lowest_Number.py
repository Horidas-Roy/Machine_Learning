n = int(input())
l = list(map(int,input().split()))
idx = l.index(min(l))
print(min(l),idx+1)