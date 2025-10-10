n = int(input())
votes = [input() for i in range(n)]
if votes.count("YES") >= votes.count("NO"):
    print("ACCEPT")
else:
    print("REJECT")