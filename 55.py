f=open(R"D:\pythonn\files\test1.txt.txt","r")
l,u,d,sc,sp,enter=0,0,0,0,0,0
for i in f.read():
        if i.islower():
                l+=1
        elif i.isupper():
                u+=1        
        elif i.isspace():
                sp+=1
        elif i.isdigit():
                d+=1
        elif i=="\n":
                enter+=1        
        else:
                sp+=1                       
print(f"your input have lower={l} and upper={u} and space={sp} and \n digit = {d} and special charachters = {sc} have enter = {enter}")                 
