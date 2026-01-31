a=[1,23,19,16,18,24,"mohammad","abalfazl",1,1]
a.remove(23)
a.remove(18)
a.insert(5,"arash")
for i in range(len(a)) :
        if a[i] == 1 :
                a.remove(1)
                a.insert(i,"ali")
print(a)          