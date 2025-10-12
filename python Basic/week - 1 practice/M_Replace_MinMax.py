n = int(input())
l = list(map(int,input().split()))
mnIdx = l.index(min(l))
mxIdx = l.index(max(l))

l[mnIdx],l[mxIdx] = l[mxIdx],l[mnIdx]

for num in l:
    print(num,end=" ")