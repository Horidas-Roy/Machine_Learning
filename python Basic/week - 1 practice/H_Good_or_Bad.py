n = int(input())

for i  in range(0,n):
    num = input()
    if "010" in num or "101" in num:
        print("Good")
    else:
        print("Bad")