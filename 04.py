for i in range(1,50,1):
      if(i%3==0 and i%5==0):
            print("fizzbuzz") 
      if (i%3==0):
            print("fizz")
            continue
      if (i%5==0):
            print("buzz")
            continue
      print(i)