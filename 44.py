import random 
pc=random.randint(1,100)
counter=0
user=int(input("enter the number =->  "))
if pc==user :
        print("you win 👍👍👍")
        counter+=1
elif pc>user :
        print("bozorg tare tar hast ")
        counter+=1
elif pc<user :
        print("kochik  tar hast ")
        counter+=1
while pc!=user:
        user=int(input("enter the number =->  "))
        if pc==user :
                print("you win 👍👍👍")
                counter+=1
        elif pc>user :
                print("bozorg tare ")
                counter+=1
        elif pc<user :
                print("kochich tare  ")
                counter+=1
print(f"you win after {counter}")                

