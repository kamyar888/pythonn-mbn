import csv
from statistics import mean 
f=open(R"C:\Users\kamsh\OneDrive\Documents\test2.csv","r")
x=csv.reader(f)
list1=[]
for i in x :
        name=i[0]
        for j in i[1:] :
                list1.append(float(j))
        print(f"your name :  {name} and your avg = {mean(list1)}")