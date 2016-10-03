# test cases for basic row operations
from plane import Plane
from vector import Vector
from linsys import LinearSystem

p0 = Plane(normal_vector=Vector([float('1'), float('1'), float('1')]), constant_term=float('1'))
p1 = Plane(normal_vector=Vector([float('0'), float('1'), float('0')]), constant_term=float('2'))
p2 = Plane(normal_vector=Vector([float('1'),float('1'),float('-1')]), constant_term=float('3'))
p3 = Plane(normal_vector=Vector([float('1'),float('0'),float('-2')]), constant_term=float('2'))

s = LinearSystem([p0,p1,p2,p3])
s.swap_rows(0,1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 1 failed'

s.swap_rows(1,3)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print 'test case 2 failed'

s.swap_rows(3,1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 3 failed'

s.multiply_coefficient_and_row(1,0)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 4 failed'

s.multiply_coefficient_and_row(-1,2)
if not (s[0] == p1 and
        s[1] == p0 and
        s[2] == Plane(normal_vector=Vector([float('-1'),float('-1'),float('1')]), constant_term=float('-3')) and
        s[3] == p3):
    print 'test case 5 failed'

s.multiply_coefficient_and_row(10,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector([float('10'),float('10'),float('10')]), constant_term=float('10')) and
        s[2] == Plane(normal_vector=Vector([float('-1'),float('-1'),float('1')]), constant_term=float('-3')) and
        s[3] == p3):
    print 'test case 6 failed'

s.add_multiple_times_row_to_row(0,0,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector([float('10'),float('10'),float('10')]), constant_term=float('10')) and
        s[2] == Plane(normal_vector=Vector([float('-1'),float('-1'),float('1')]), constant_term=float('-3')) and
        s[3] == p3):
    print 'test case 7 failed'

s.add_multiple_times_row_to_row(1,0,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector([float('10'),float('11'),float('10')]), constant_term=float('12')) and
        s[2] == Plane(normal_vector=Vector([float('-1'),float('-1'),float('1')]), constant_term=float('-3')) and
        s[3] == p3):
    print 'test case 8 failed'

s.add_multiple_times_row_to_row(-1,1,0)
if not (s[0] == Plane(normal_vector=Vector([float('-10'),float('-10'),float('-10')]), constant_term=float('-10')) and
        s[1] == Plane(normal_vector=Vector([float('10'),float('11'),float('10')]), constant_term=float('12')) and
        s[2] == Plane(normal_vector=Vector([float('-1'),float('-1'),float('1')]), constant_term=float('-3')) and
        s[3] == p3):
    print 'test case 9 failed'