start=int(input("enter the number what you want start= "))
end=int(input("enter the number what you want end = "))
even=0
odd=0
for i in range(start,end,1):
      if (i%2==0):
            even=even+1
      elif (i%2!=0):
            odd=odd+1
print(f"bitween {start} and {end} you have zoj={even} and fard={odd}")                  
