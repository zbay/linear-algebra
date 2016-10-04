from plane import Plane
from vector import Vector
from linsys import LinearSystem

p1 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector([float('0'),float('1'),float('1')]), constant_term=float('2'))
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2):
    print 'test case 1 failed'

p1 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('2'))
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == Plane(constant_term=float('1'))):
    print 'test case 2 failed'

p1 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector([float('0'),float('1'),float('0')]), constant_term=float('2'))
p3 = Plane(normal_vector=Vector([float('1'),float('1'),float('-1')]), constant_term=float('3'))
p4 = Plane(normal_vector=Vector([float('1'),float('0'),float('-2')]), constant_term=float('2'))
s = LinearSystem([p1,p2,p3,p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2 and
        t[2] == Plane(normal_vector=Vector([float('0'),float('0'),float('-2')]), constant_term=float('2')) and
        t[3] == Plane()):
    print 'test case 3 failed'

p1 = Plane(normal_vector=Vector([float('0'),float('1'),float('1')]), constant_term=float('1'))
p2 = Plane(normal_vector=Vector([float('1'),float('-1'),float('1')]), constant_term=float('2'))
p3 = Plane(normal_vector=Vector([float('1'),float('2'),float('-5')]), constant_term=float('3'))
s = LinearSystem([p1,p2,p3])
t = s.compute_triangular_form()
print s
print t
if not (t[0] == Plane(normal_vector=Vector([float('1'),float('-1'),float('1')]), constant_term=float('2')) and
        t[1] == Plane(normal_vector=Vector([float('0'),float('1'),float('1')]), constant_term=float('1')) and
        t[2] == Plane(normal_vector=Vector([float('0'),float('0'),float('-9')]), constant_term=float('-2'))):
    print 'test case 4 failed'