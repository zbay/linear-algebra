from vector import Vector
from plane import Plane

#question 1
plane1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
plane2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)
print "Plane 1 and Plane 2 intersection: " + plane1.intersection(plane2)

#question 2
plane3 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
plane4 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)
print "Plane 3 and Plane 4 intersection: " + plane3.intersection(plane4)

#question 3
plane5 = Plane(Vector([-7.926, 8.625, -7.217]), -7.952)
plane6 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)
print "Plane 5 and Plane 6 intersection: " + plane5.intersection(plane6)