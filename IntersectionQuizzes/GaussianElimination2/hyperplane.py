from decimal import Decimal, getcontext
from myDecimal import MyDecimal
from vector import Vector
from copy import deepcopy

getcontext().prec = 30

class Hyperplane(object):
    NO_NONZERO_ELTS_FOUND_MSG = "No nonzero elements found!"
    EITHER_DIM_OR_NORMAL_VEC_MUST_BE_PROVIDED_MSG = "You must provide a dimension or a normal vector."
    
    def __init__(self, dimension=None, normal_vector=None, constant_term=None):
        if not dimension and not normal_vector:
            raise Exception(self.EITHER_DIM_OR_NORMAL_VEC_MUST_BE_PROVIDED_MSG)
        elif not normal_vector:
            self.dimension = dimension
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        else:
            self.dimension = normal_vector.dimension
        self.normal_vector = normal_vector
        
        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)
        
        self.set_basepoint()

    def __getitem__(self,index):
        if index == self.dimension:
            return Decimal(self.constant_term)
        else:
            return Decimal(self.normal_vector[index])
            
    def __setitem__(self,index,value):
        if index == self.dimension:
            self.constant_term = value
        else:
            self.normal_vector[index] = value
    
    def __eq__(self, p):
        if self.dimension != p.dimension:
            return False
        for i in range(self.dimension):
            if not MyDecimal(float(self.normal_vector[i]) - float(p.normal_vector[i])).is_near_zero():
                return False
        if not MyDecimal(self.constant_term - p.constant_term).is_near_zero():
            return False
        return True
        
    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Hyperplane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = float(c)/float(initial_coefficient)
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Hyperplane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Hyperplane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output
    
    def is_parallel(self, otherLine): 
        return self.normal_vector.parallel_to(otherLine.normal_vector)

    def is_equal(self, otherLine):
        connectorVector = self.basepoint.subtract(otherLine.basepoint)
        return connectorVector.orthogonal_to(self.normal_vector)

    def invalid_plane(self):
        if not MyDecimal(self.constant_term).is_near_zero():
            for i in range(self.dimension):
                if not MyDecimal(self[i]).is_near_zero():
                    return False
            return True
        return False
       
    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Hyperplane.NO_NONZERO_ELTS_FOUND_MSG)
        