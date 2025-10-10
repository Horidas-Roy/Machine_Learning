msg = list(input().split())
dict = {}
for word in msg:
    if word in ("ai", "data", "model", "learn", "train", "neural"):
        dict[word] = dict.get(word,0)+1
        
if len(dict)>= 2:
    print("AI Detected")
else:
    print("Not AI Related")