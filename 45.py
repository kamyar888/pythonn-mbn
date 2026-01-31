import random 
list1=["s","gh","k"]
u=0
p=0
for i in range (10):
        pc=random.choice(list1)
        user=input("enter your choice = ")
        if user==pc :
                print("equal😏😏😏")
        elif (user=="k" and pc=="s") or (user=="s" and pc=="gh") or (user=="gh" and pc =="k") :
                print(f"you win you: {user} and pc :{pc} 😜😜😜 ")
                u+=1
        else:
                p+=1
                print(f"you lose you :{user} and pc :{pc} 🤬🤬🤬")
if u>p :
        print(f"you win you :{u} pc:{p} 😜😜😜")
elif p>u :                               
        print(f"you lose you :{u} pc:{p} 🤬🤬🤬")
else :
        print(f"equal you :{u} pc:{p} 😏😏😏")