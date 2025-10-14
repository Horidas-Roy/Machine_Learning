n = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.extend(a)
for i in b:
    print(i,end=" ")
