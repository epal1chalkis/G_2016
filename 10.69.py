#askisi 10.69
eidos = input("dose an o eidos kafe (1 an einai A)(2 an einai B)" )
posotita = input ("dose tin posotita tou kafe se gramaria")
if eidos == 1:
    if posotita >= 400:
        pliromi = (0.95 * posotita)/100
    else:
        pliromi = (0.85 * posotita)/100
if eidos == 2:
    if posotita <= 500:
        pliromi = (1.2 * posotita)/100
    else:
        pliromi = posotita/100
print "tha plirosi o pelatis", pliromi
