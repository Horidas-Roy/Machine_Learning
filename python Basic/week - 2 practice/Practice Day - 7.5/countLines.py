try:
    with open("story.txt","r") as file:
        lines = file.readlines()
        print(len(lines))
except Exception:
    print(Exception)