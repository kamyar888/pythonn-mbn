f=open(R"D:\pythonn\files\test1.txt.txt","r")
for i in f.read().split():
        if i[0]=="a":
                print(i)