n,m = map(int,input().split())
l = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))

# A = l.copy()
# A &= a
# B = l.copy()
# B &= b
# print(len(A)-len(B))

print(sum((i in a) - (i in b) for i in l))
