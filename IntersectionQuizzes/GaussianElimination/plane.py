from decimal import Decimal, getcontext
from myDecimal import MyDecimal

from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = [0]*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = float(c)/float(initial_coefficient)
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
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
            initial_index = Plane.first_nonzero_index(n)
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

    def intersection(self, otherLine):
        if self.is_equal(otherLine):
            return "The planes are equal and intersect at every point."
        elif self.is_parallel(otherLine):
            return "The planes are parallel and do not intersect."
        else:
            return "These planes intersect somewhere, either in a line or at a point."
    
    def point_intersection(self, line2, line3):
        system = self.matricise([self, line2, line3])
        system = self.reduce_matrix(system)
        solution_coordinates = self.solve(system)
        return solution_coordinates
        
    def solve(self, system):
        #solve for z: z = c
        z = Decimal(round(system[2][3], 3))
        solution_coordinates = [0,0, round(system[2][2], 3)]
        #solve for y: c -= z * x3
        y = Decimal(round(system[1][3] - z*system[1][2], 3))
        #solve for x: c -= ((z * x3) + (y*x2))
        x = Decimal(round(system[0][3] - ((z*system[0][2]) +(y*system[0][1]))))
        return "( " + str(x) + ", " + str(y) + ", " + str(z) + " )"
    
    def matricise(self, rows):
        matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(3):
            currentRow = rows[i]
            normVector = currentRow.normal_vector
            rowConstant = currentRow.constant_term
            for j in range(3):
                matrix[i][j] = Decimal(normVector[j])
            matrix[i][3] = rowConstant
        return matrix
                
    def reduce_matrix(self, matrix):
        # get [0][0] to 1, [1][0] to 0, [2][0] to 0, [1][1] to 1, [2][1] to 0, and [2][1] to 0 in that order.
        # if stuck, swap. If [0][0] is 0, swap with the highest row with a nonzero in that column
        # If [1][1] is 0, swap with row 3 
            
        #get [0][0] to 1
        if matrix[0][0] == 0:
            if matrix[1][0] != 0:
                matrix = self.swap_rows(matrix, 0, 1)
            elif matrix[2][0] != 0:
                matrix = self.swap_rows(matrix, 0, 2)
        
        leadCoefficient = matrix[0][0]
        for i in range(4):
            matrix[0][i] /= leadCoefficient
        
        #get [1][0] to 0
        leadCoefficient = matrix[1][0]
        for i in range(4):
            matrix[1][i] -= leadCoefficient*matrix[0][i]
        
        #get [2][0] to 0
        leadCoefficient = matrix[2][0]
        for i in range(4):
            matrix[2][i] -= leadCoefficient*matrix[0][i]
        
        #get [1][1] to 1
        if matrix[1][1] == 0:
            if matrix[2][1] != 0:
                matrix = self.swap_rows(matrix, 1, 2)
        leadCoefficient = matrix[1][1]
        for i in range(3):
            matrix[1][i+1] /= leadCoefficient
        
        #get [2][1] to 0
        leadCoefficient = matrix[2][1]
        for i in range(4):
            matrix[2][i] -= leadCoefficient*matrix[1][i]
        
        #get [2][2] to 1
        leadCoefficient = matrix[2][2]
        for i in range(2):
            matrix[2][i+2] /= leadCoefficient
        
        return matrix
        
    def swap_rows(self, matrix, row1, row2):
        tempRow = matrix[row1]
        matrix[row1] = row2
        matrix[row2] = tempRow
        return matrix
        

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)