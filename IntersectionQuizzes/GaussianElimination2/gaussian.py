from plane import Plane
from vector import Vector
from linsys import LinearSystem
from decimal import Decimal

#question 1
p1 = Plane(normal_vector=Vector([float('5.862'),float('1.178'),float('-10.366')]), constant_term=float('-8.15'))
p2 = Plane(normal_vector=Vector([float('-2.931'),float('-0.589'),float('5.183')]), constant_term=float('-4.075'))
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
p1 = Plane(normal_vector=Vector([float('5.262'),float('2.739'),float('-9.878')]), constant_term=float('-3.441'))
p2 = Plane(normal_vector=Vector([float('5.111'),float('6.358'),float('7.638')]), constant_term=float('-2.152'))
p3 = Plane(normal_vector=Vector([float('2.016'),float('-9.924'),float('-1.367')]), constant_term=float('-9.278'))
p4 = Plane(normal_vector=Vector([float('2.167'),float('-13.543'),float('-18.883')]), constant_term=float('-10.567'))
s = LinearSystem([p1,p2,p3,p4])
r = s.solve_system()
print r