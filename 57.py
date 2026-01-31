f=open(R"D:\pythonn\files\test1.txt.txt","r")
vowel="UuAaIiEeOo"
c=0
for i in f.read():
        if i in vowel:
                c+=1
print(c)                