pixels = list(map(int,input().split()))
avg_brightness = sum(pixels)/len(pixels)

if avg_brightness < 85 :
    print("Dark Image")
elif avg_brightness <= 170:
    print("Normal Image")
else:
    print("Bright Image")
