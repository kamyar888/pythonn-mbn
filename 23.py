list1=input("enter the numbers = ").split()
mazrab=[]
for i in list1 :
        if int(i)%5==0 or int(i)%3==0 :
                mazrab.append(int(i))
mazrab.sort()                
print(mazrab)                       