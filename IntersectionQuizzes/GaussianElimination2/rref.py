from plane import Plane
from vector import Vector
from linsys import LinearSystem
from decimal import Decimal

p1 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector([float('0'),float('1'),float('1')]), constant_term=float('2'))
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector([float('1'),float('0'),float('0')]), constant_term=float('-1')) and
        r[1] == p2):
    print 'test case 1 failed'

p1 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term=float('2'))
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == p1 and
        r[1] == Plane(constant_term=float('1'))):
    print 'test case 2 failed'

p1 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector([float('0'),float('1'),float('0')]), constant_term=float('2'))
p3 = Plane(normal_vector=Vector([float('1'),float('1'),float('-1')]), constant_term=float('3'))
p4 = Plane(normal_vector=Vector([float('1'),float('0'),float('-2')]), constant_term=float('2'))
s = LinearSystem([p1,p2,p3,p4])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector([float('1'),float('0'),float('0')]), constant_term=float('0')) and
        r[1] == p2 and
        r[2] == Plane(normal_vector=Vector([float('0'),float('0'),float('1')]), constant_term=float('-1')) and
        r[3] == Plane()):
    print 'test case 3 failed'

p1 = Plane(normal_vector=Vector([float('0'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector([float('1'),float('-1'),float('1')]), constant_term=float('2'))
p3 = Plane(normal_vector=Vector([float('1'),float('2'),float('-5')]), constant_term=float('3'))
s = LinearSystem([p1,p2,p3])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector([float('1'),float('0'),float('0')]), constant_term=float(Decimal('23')/Decimal('9'))) and
        r[1] == Plane(normal_vector=Vector([float('0'),float('1'),float('0')]), constant_term=float(Decimal('7')/Decimal('9'))) and
        r[2] == Plane(normal_vector=Vector([float('0'),float('0'),float('1')]), constant_term=float(Decimal('2')/Decimal('9')))):
    print 'test case 4 failed'