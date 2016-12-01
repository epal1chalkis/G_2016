#10.72.
el=int(input("dwse thn hlikia tou odigou"))
ep=int(input("dwse tous ipous"))
if ((el >= 18) and (el <= 65)):
    if ep<=7:
        asf=(152*15)/100
        sas=152+asf
    elif ep<=10:
        asf=(185*15)/100
        sas=185+asf
    elif ep<=12:
        asf=(211*15)/100
        sas=211+asf
    elif ep<=14:
        asf=(224*15)/100
        sas=224+asf
else:
    if ep<=7:
        asf=(152*5)/100
        sas=152+asf
    elif ep<=10:
        asf=(185*5)/100
        sas=185+asf
    elif ep<=12:
        asf=(211*5)/100
        sas=211+asf
    elif ep<=14:
        asf=(224*5)/100
        sas=224+asf
print ("ta asfalistra einai",sas)
