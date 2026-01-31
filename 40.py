dict1={"soghra":"09122572080",
       "asghar":"09906161871",
       }
def daftarchetelephone():
        print("if you want to know number just give name :\n" 
        "if you want to del name and number press :1\n"
        "if you want to add name and number just press :2 \n")
        q=input("enter the name to give number to you😎😎😎 : ")
        if q in dict1.keys():
                print(dict1[q])
                a=input("do you want to continuo🤔🤔🤔 ??? ")
                if a=="yes" :
                     daftarchetelephone()  
        elif q=="1":
                s=input("enter what key wat yo want to del🤐🤐🤐::::   ")
                del dict1[s]
                print(dict1)
                daftarchetelephone()             
        elif q=="2" :
                print("i dont have any number for this name do you want to added to daftarche telefon")
                r=input("do you want to add =  ")
                if r=="yes" :
                        q=input("enter the name to give number to you : ")
                        n=int(input("enter the number =->"))
                        dict1.update({q:n})
                        print(dict1)
                elif r=="no":
                        print("ok bro gomsho pas maraz dari mage ???🤬🤬🤬🤬")    
daftarchetelephone()                                        