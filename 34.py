dict1={"red":"قرمز","water":"اب","knife":"چاقو","sky":"اسمان",
       "poll":"نظرسنجی","chair":"صندلی","soft":"مبل","carpet":"فرش",
       "notebook":"دفتر","pen":"حودکار","love":"تو"}
word=input("enter word ?we translate it !!! =->")
if  word in dict1.keys() :
        print(dict1[word])
else :
        print("ops i dont have difinition !!!")
        q=input("do you know meaning ????")
        if q=="yes" :
                g=input("give it to me ???")
                dict1.update({word:g})
                print(dict1)
        else:
                print("thanks...")        