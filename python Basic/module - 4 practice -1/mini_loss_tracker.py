n = int(input())
target = float(input())
loss = [float(input()) for i in range(n)]
avg_loss = sum(loss)/n

if avg_loss <= target:
    print("PASS")
else:
    print("RETRY")