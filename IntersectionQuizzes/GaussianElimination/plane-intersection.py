from vector import Vector
from plane import Plane

'''
#quiz 1
plane1 = Plane(Vector([-1, 1, 1]), -2)
plane2 = Plane(Vector([1, -4, 4]), 21)
plane3 = Plane(Vector([7, -5, -11]), 0)
print "Plane 1, 2 and 3 intersection at a point: " + plane1.intersection3(plane2, plane3)
'''

#quiz 2: adjust for possibility of no solution (0=1), for example, and for a redundant variable that renders the intersection a line rather than a point

#question 1
plane1 = Plane(Vector([1, -2, 1]), -1)
plane2 = Plane(Vector([1, 0, -2]), 2)
plane3 = Plane(Vector([-1, 4, -4]), 0)
print "Plane 1, 2 and 3 intersection: " + plane1.intersection3(plane2, plane3)

#question 2
plane1 = Plane(Vector([0, 1, -1]), 2)
plane2 = Plane(Vector([1, -1, 1]), 2)
plane3 = Plane(Vector([3, -4, 1]), 1)
print "Plane 4, 5 and 6 intersection: " + plane1.intersection3(plane2, plane3)

#question 3
plane1 = Plane(Vector([1, 2, 1]), -1)
plane2 = Plane(Vector([3, 6, 2]), 1)
plane3 = Plane(Vector([-1, -2, -1]), 1)
print "Plane 7, 8 and 9 intersection: " + plane1.intersection3(plane2, plane3)
