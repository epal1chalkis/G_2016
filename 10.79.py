#10.79
tipos = raw_input ("Dose A an einai fortigo, Dose B an einai epivatiko i dose C an einai dikiklo: ")
mikos = input ("Dose to mikos tou oximatos se ekatosta: ")
thesi = raw_input ("Dose an i thesi tou odigou einai A i B: ")
if tipos == "A":
    xreosi_oximatos = mikos * 0.6
if tipos == "B":
    xerosi_oximatos = mikos * 0.4
if tipos == "C":
    xreosi_oximatos = mikos * 0.2
if thesi == "A":
    xreosi = (xreosi_oximatos)*0.23 + xreosi_oximatos + 35
if thesi == "B":
    xreosi = (xreosi_oximatos)*0.23 + xreosi_oximatos + 25   
print "tha plirosei", xreosi
