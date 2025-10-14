from functools import reduce
n = int(input())
l = list(map(float,input().split()))
sum = reduce(lambda x,y:x+y,l)
avg = round(sum/n,7)

print(f"{avg:.7f}")