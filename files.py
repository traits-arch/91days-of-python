open("demotext.txt", "a").write("\nHave a good day btw")
f = open("demotext.txt", "r")
data = f.read()
line1 = f.readline(7)
print(data)
print(type(data))
print(line1)
f.close()

with open("demotext.txt", "r") as f:
    data= f.read()
    print(data)
    f.close()
with open("demotext.txt", "a") as f:
    f.write("\n And dont forget to update github")
    print(data)
    f.close()

with open("demotext.txt", "r") as f:
    data= f.read()
    data= data.replace("Have a good day btw", "Have a great day")
    print(data)
    f.close()

with open("demotext.txt", "r+") as f:
    data= f.read()
    if data.find("good day") != -1:
       print("Found")
    else:
         print("Not Found")
    f.close()
#check what line
def check_line():
    word= str(input("Enter the word you want to search: "))
    data= True
    line_no=1
    with open("demotext.txt","r") as f:
        while data:
            data= f.readline()
            if(word in data):
                print(line_no)
                return
            else:
                line_no += 1
    return -1
print(check_line())
