#10.74
x = input ("Dose ton aksona x tou simiou a ")
y = input ("Dose ton aksona y tou simiou a ")
if x > 0 and y > 0:
    print "proto tetartimorio"
elif  x < 0 and y > 0:
    print "deytero tetartimorio"
elif x < 0 and y < 0:
    print "trito tetartimorio"
elif x > 0 and y < 0:
    print "tetarto tetartimorio"
elif y == 0:
    print "anikei ston aksona x"
elif x == 0:
    print "anikei ston aksona y"
