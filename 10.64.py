#askisi 10.64
import math
x = input ("dose ton arithmo x ")
if x > 5:
    f_x = (x+2)/(x**3 + 1)
elif x ==5:
    f_x = x**2
else:
    f_x = math.sqrt (x + 2)
print "to f(x) einai",f_x
