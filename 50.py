mah={
        "farvardin":"31",
        "ordibehesht":"31",
        "khordad":"31",
        "tir":"31",
        "mordad":"31",
        "shahrivar":"31",
        "mehr":"30",
        "aban":"30",
        "azar":"30",
        "dey":"30",
        "bahman":"30",
        "esfand":"29",
        }
daramad={
        "farvardin":"",
        "ordibehesht":"",
        "khordad":"",
        "tir":"",
        "mordad":"",
        "shahrivar":"",
        "mehr":"",
        "aban":"",
        "azar":"",
        "dey":"",
        "bahman":"",
        "esfand":"",
        }
ghkn=int(input("enter the gheymat non bastani -=> "     ))
ghkb=int(input("enter the gheymat mavad bastani -=> "   ))
ghfb=int(input("enter the gheymat frosh bastani =->  "  ))
tfb=int(input("enter the tedad frosh bastani -=>  "     ))
chm=input("enter the mah =->  " )
def bastani():
        stk=int(ghkb)-int(ghkn)+int(ghkb)
        kol=int(stk)*int(tfb)
        if chm in mah.keys() :
                 print(sodm)
                 roz=mah.keys(chm)
                 sodm=int(roz)*kol
                 daramad.values(sodm)
                 
        print("agr mikhai kol daramd va sod salianato hesab kni metoni add 1 ro bezani :   ")
        q=int(input("mikhay???  "))
        if q==1 :
                12*bastani()         
bastani()                                