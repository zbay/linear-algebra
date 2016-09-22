from decimal import Decimal, getcontext
from myDecimal import MyDecimal

from vector import Vector

getcontext().prec = 30

class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector: # default normal vector is (0,0)
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term: # default constant term is 0
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()
        
    def __iter__(self):
        return iter(self.normal_vector.coordinates)


    def set_basepoint(self): #derives a point on the line to use as an anchor, b setting one of the two variables to zero
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n) # 0 if x coefficient is nonzero, 1 if y component is nonzero
            initial_coefficient = n[initial_index] # leading coefficient

            basepoint_coords[initial_index] = float(c)/float(initial_coefficient) # divide the constant by the initial coefficient to get the base coordinate
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG: # if normal vector is zero, no basepoint
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
            initial_index = Line.first_nonzero_index(n)
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
        normalSelf = self.normal_vector
        otherSelf = otherLine.normal_vector
        return normalSelf.parallel_to(otherSelf)
    
    def is_equal(self, otherLine): # the line connecting the two normal vectors is parallel to both
        selfBasepoint = self.basepoint
        otherBasepoint = otherLine.basepoint
        connectorVector = selfBasepoint.subtract(otherBasepoint)
        normalSelf = self.normal_vector
        return normalSelf.orthogonal_to(connectorVector)
    
    def intersection(self, otherLine):
        if self.is_equal(otherLine):
            return "The lines are equal, intersecting at every point."
        elif self.is_parallel(otherLine):
            return "The lines are parallel and do not intersect."
        else:   # step 1: divide an equation by first leading coefficient
            selfCoordinates = self.normal_vector.coordinates
            selfConstant = float(self.constant_term)
            otherCoordinates = otherLine.normal_vector.coordinates
            otherConstant = float(otherLine.constant_term)
            firstDivisor = 1
            if Line.first_nonzero_index(self) == 0:
                firstDivisor = selfCoordinates[0]
            elif Line.first_nonzero_index(otherLine) == 0:
                firstDivisor = otherCoordinates[1]
                temp = selfCoordinates
                tempConstant = selfConstant
                selfCoordinates = otherCoordinates
                selfConstant = otherConstant
                otherCoordinates = temp
                otherConstant = tempConstant
            else:
                return Vector([0, 0])
            selfConstant /= firstDivisor
            selfCoordinates[0] /= firstDivisor
            selfCoordinates[1] /= firstDivisor
                
            # step 2: subtract coefficient * new equation 1 coefficient from everything in equation 2
            otherDivisor = otherCoordinates[0]
            otherCoordinates[0] -= otherDivisor * selfCoordinates[0]
            otherCoordinates[1] -= otherDivisor * selfCoordinates[1] 
            otherConstant -= otherDivisor * selfConstant
            
            # step 3: solve for y
            intersectionCoordinates = [0, otherConstant / otherCoordinates[1]]
            # step 4: plug in y solution to solve for x
            selfConstant -= intersectionCoordinates[1] * selfCoordinates[1]
            intersectionCoordinates[0] = selfConstant / selfCoordinates[0]
            return "( " + str(intersectionCoordinates[0]) + ", " + str(intersectionCoordinates[1]) + " )"
            

    @staticmethod
    def first_nonzero_index(iterable): # iterates through vector to return index of first nonzero term OR throws an exception
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)