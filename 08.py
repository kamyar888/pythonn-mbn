x1=1
x2=1
print(x1)
print(x2)
c=0
for i in range(1,50,1):
      c=x1+x2     
      print(c,end=' ^  ')
      x1=x2
      x2=c
      

