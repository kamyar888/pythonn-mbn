list1=input("enter the numbers").split()
even=[]
odd=[]
for i in list1 :
        if float(i)%2==0 :
                even.append(float(i))
        else :
                odd.append(i)
print(f"this is even ={even}")
print(f"this is odd ={odd}")                        
