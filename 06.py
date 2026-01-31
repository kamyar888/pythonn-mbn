a=input("enter what dama you want to convert =  ")
x=int(a[:-1])
if (a[-1]=="f"):
      y=x-32
      print(f"the {a} farenhieght is {y}celsios ")
elif (a[-1]=="c"):
      y=x+32
      print(f"the {a} celesios is {y}farenhight ")      