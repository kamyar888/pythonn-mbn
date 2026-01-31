list1=input("enter the key and values = ").split()
dict1={}
for i in list1 :
        dict1.update({i[0]:int(i[1:])})
t=tuple(dict1.values())        
print(f"sum = ({sum(t)})  min = ({min(t)})  max = ({max(t)})")      