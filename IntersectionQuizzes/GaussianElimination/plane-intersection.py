from vector import Vector
from plane import Plane

#question 1
plane1 = Plane(Vector([-1, 1, 1]), -2)
plane2 = Plane(Vector([1, -4, 4]), 21)
plane3 = Plane(Vector([7, -5, -11]), 0)
print "Plane 1, 2 and 3 intersection at a point: " + plane1.point_intersection(plane2, plane3)