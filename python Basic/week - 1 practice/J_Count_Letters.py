s = input()
dic = {}
for ch in s:
    dic[ch] = dic.get(ch,0)+1

for key in sorted(dic.keys()):
    print(key,":",dic[key])