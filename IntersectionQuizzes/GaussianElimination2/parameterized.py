from plane import Plane
from vector import Vector
from linsys import LinearSystem
from decimal import Decimal

#question 1
p1 = Plane(normal_vector=Vector([float('0.786'),float('0.786'),float('0.588')]), constant_term=float('-0.714'))
p2 = Plane(normal_vector=Vector([float('-0.131'),float('-0.131'),float('0.244')]), constant_term=float('0.319'))
s = LinearSystem([p1,p2])
r = s.solve_system()
print r

#question 2
p1 = Plane(normal_vector=Vector([float('8.631'),float('5.112'),float('-1.816')]), constant_term=float('-5.113'))
p2 = Plane(normal_vector=Vector([float('4.315'),float('11.132'),float('-5.27')]), constant_term=float('-6.775'))
p3 = Plane(normal_vector=Vector([float('-2.158'),float('3.01'),float('-1.727')]), constant_term=float('-0.831'))
s = LinearSystem([p1,p2, p3])
r = s.solve_system()
print r

#question 3
p1 = Plane(normal_vector=Vector([float('0.935'),float('1.76'),float('-9.365')]), constant_term=float('-9.955'))
p2 = Plane(normal_vector=Vector([float('0.187'),float('0.352'),float('-1.873')]), constant_term=float('-1.991'))
p3 = Plane(normal_vector=Vector([float('0.374'),float('0.704'),float('-3.746')]), constant_term=float('-3.982'))
p4 = Plane(normal_vector=Vector([float('-0.561'),float('-1.056'),float('5.619')]), constant_term=float('5.973'))
s = LinearSystem([p1,p2,p3,p4])
r = s.solve_system()
print r