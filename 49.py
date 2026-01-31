num=int(input("meghdar ab masrafi ro bar hasb metr mohab begoiid =->  "))
def bahaab():
        baha=int(num)*111.000
        if int(num)<21 :
                print("shoma az pardakht hazineh ab masrafi moaf hastid ...!")
        elif(int(num)>21 and int(num)<41) :
                jarimeh=baha*0.05
                x=baha+jarimeh
                print(f"shoma ba ({num}) masraf bayad ba ehtesab 5% jarime {x} bayad pardakht knid")
        elif(int(num)>41) :
                jarimeh=baha*0.1
                x=baha+jarimeh
                print(f"shoma ba ({num}) masraf bayad ba ehtesab 10% jarime {x} bayad pardakht knid")        
bahaab()                