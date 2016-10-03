#goals: go to udacity. remember that swap rows and the two after it might not work

from decimal import Decimal, getcontext
from myDecimal import MyDecimal
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30

class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
       temp = self.planes[row1]
       self.planes[row1] = self.planes[row2]
       self.planes[row2] = temp


    def multiply_coefficient_and_row(self, coefficient, row):
        for i in range(self.dimension+1):
            self.planes[row][i] *= coefficient


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        for i in range(self.dimension+1):
            self.planes[row_to_be_added_to][i] += coefficient*self.planes[row_to_add][i]

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret

'''
p0 = Plane(normal_vector=Vector([float('1'),float('1'),float('1')]), constant_term=float('1'))
p1 = Plane(normal_vector=Vector([float('0'),float('1'),float('0')]), constant_term=float('2'))
p2 = Plane(normal_vector=Vector([float('1'),float('1'),float('-1')]), constant_term=float('3'))
p3 = Plane(normal_vector=Vector([float('1'),float('0'),float('-2')]), constant_term=float('2'))

s = LinearSystem([p0,p1,p2,p3])

#print s.indices_of_first_nonzero_terms_in_each_row()
print s[0][0]
#print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
#print len(s)
#print s

s[0] = p1
#print s

print MyDecimal('1e-9').is_near_zero()
print MyDecimal('1e-11').is_near_zero()
'''