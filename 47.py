import random
a=set()
for  i in range(10):
        if len(a)!=10 :
                b=random.randint(1,100)
                a.add(b)
print(a)        