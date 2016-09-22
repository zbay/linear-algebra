from vector import Vector
from line import Line

#question 1
line1 = Line(Vector([4.046, 2.836]), 1.21)
line2 = Line(Vector([10.115, 7.09]), 3.025)
print "Line 1 and Line 2 intersection: " + line1.intersection(line2)

#question 2
line3 = Line(Vector([7.204, 3.182]), 8.68)
line4 = Line(Vector([8.172, 4.114]), 9.883)
print "Line 3 and Line 4 intersection:" + line3.intersection(line4)

#question 3
line5 = Line(Vector([1.182, 5.562]), 6.744)
line6 = Line(Vector([1.773, 8.343]), 9.525)
print "Line 5 and Line 6 intersection: " + line5.intersection(line6)