with open("names.txt","r") as file:
    content = file.read().strip().split()
    names = sorted(list(set([name.title() for name in content])))
with open("clean_names.txt",'w') as file:
    for name in names:
        file.write(f"{name}\n")