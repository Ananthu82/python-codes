with open("output.txt","w")as file:
    file.write("knock knock\n")
    file.close()
with open("output.txt","a")as file:
    file.write("who's there\n")
    file.close()
with open("output.txt","r")as file:
    print(file.read())
