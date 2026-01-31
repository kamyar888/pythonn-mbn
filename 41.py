import random 
print("if you whant to gnerate password press :1\n"
      "if you whant to have valut password press :2")
c=int(input("adad khud ra begoiid  = "))
if c==1:
        q=int(input("mikhay chand harf basheh  = "))
        def generate():
                list1=[
                        1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%","^","&","*","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                        ]
                list2=[]
                a=0
                for i in range(q):
                        x=random.choice(list1)
                        list2.append(x)
                for i in list2:
                        print(i,end='')
                print(a) 
        generate()
elif c==2 :
        def generatew():
                w=int(input("bego chand ta kalame mikhai == >  "))
                list1=[
                        "water","hello","transition","find","bigger","orange","red","benana","keyboard","elephent","lion","ball","Borrow","Break","Bring","Buy","able","Cancel","Change","Clean","Table","Bed","Sofa","Pillow","Blanket","Knife","Plate","Jacket","Gloves","Bag","Umbrella","Laptop","TV","Notebook","Scissors","Soap","Hairbrush","Comb","Broom","Detergent","Brush","Milk","Fruit","Sugar","Map","Bike","Bus","Salt","Egg","Vegetable","Tea","Duster","Bucket","Mop","Razor","Shower","Highlighter","Purse","Cap","Ring","Scarf","Year","Plan","Move","Connect"
                ]
                pur=set()
                list3=[]
                for i in range(w):
                        if len(list3)!=w:
                                E=random.choice(list1)
                                list3.append(E)    
                        for j in list3:
                                if list3.count(j)>1:
                                        del j 
                                
        generatew()
