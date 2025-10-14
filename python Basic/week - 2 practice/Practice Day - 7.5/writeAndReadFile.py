with open("data.txt","w+") as file:
    file.write("Learning Python is fun!")
    file.seek(0) #To return back the pointer at zeroth index
    content = file.read()
    print(content)