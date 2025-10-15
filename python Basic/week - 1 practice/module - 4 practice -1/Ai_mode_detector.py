msg = input()
msg = msg.split()

if any(word in msg for word in ["happy","joy","smile"]):
    print("Happy Mood")
elif any(word in msg for word in ["sad" ,"cry","angry"]):
    print("Sad Mood")
else:
    print("Neutral Mood")