list1=input("enter the values and keys =->   ").split()
list2=input("enter the values and keys =->   ").split()
dict1={}
dict2={}
for i in list1 :
        dict1.update({i[0]:int(i[1::])})
for i in list2 :
        dict2.update({i[0]:int(i[1::])})
print(dict1 ,dict2)        
for i in dict1.keys():
        if i in dict2.keys():
                
                print(i ,":",dict1[i]+dict2[i])
