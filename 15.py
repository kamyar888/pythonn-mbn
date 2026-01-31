a=input(("entert the string"))
space=0
lower=0
upper=0
digit=0
sc=0      
for i in a:
      if i.isspace() :
            space=+1
      elif i.islower() :
            lower+=1
      elif i.upper() :
            upper+=1
      elif i.isdigit() :
            digit+=1
      else:        
            sc+=1                 
print(f"your strings have space = {space} and have lower = {lower} and upper = {upper} and digit = {digit} and have special charectors = {sc}")

          