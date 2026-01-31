import random;
y=random.randint(1,10)
x=0
while x!=y  :
      x=int(input("enter your hads "))
      y=random.randint(1,10)
      if (x==y) :
            print("your hads its true")
      elif(x!=y) :
            print(f"your hads its {x} but the rondom int {y}")        