#goals: proofread basepoint and direction vectors. Rework string for Parameterization
#After making parameterization, figure out how to solve it

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
    
    def solve_system(self): # this assumes no free variables
        '''
        algorithm:
        if all are parallel to each other, return infinite solutions
        if any plane is invalid, indicate no solution
        for each row, starting from len(system.planes) and going to 0
            for each col from len(system.planes[0) to 0
                if a saved value exists for that column's variable, multiply it by the column variable and add it to the constant
                if the saved value doesn't exist, is the furthest left 1, and all values right except for constant are 0, save the value as the constant
            find answers
            if some variables are unassigned at the end, parameterize
        '''
        system = self.compute_rref()
        saved_solutions = ["None"] * system.planes[0].dimension
        are_parallel = True
        first_plane = system.planes[0]
        for i in range(1, len(system.planes)):
            if system.planes[i].invalid_plane():
                return "The system is invalid; there is no intersection."
            if not first_plane.is_parallel(system.planes[i]) or system.planes[i].is_blank(): #blank planes shouldn't count as parallel. They can be paramterized
                are_parallel = False
                break
        if are_parallel:
            return "The lines are parallel; the system has an infinite number of solutions."
        for i in range(len(system.planes)-1, -1, -1):
            leftmost_one = system.leftmost_one(i)
            for j in range(system.planes[0].dimension-1, -1, -1):
                if saved_solutions[j] != "None" and not MyDecimal(system[i][j]).is_near_zero():
                    system[i][system.planes[0].dimension] += saved_solutions[j] * system[i][j]
                    system[i][j] = 0
                else:
                    if j == leftmost_one:
                        saved_solutions[j] = system[i][system.planes[0].dimension]
        for i in range(len(saved_solutions)):
            if saved_solutions[i] == "None":
                copy_system = self.compute_rref()
                direction_vectors = copy_system.extract_direction_vectors() 
                basepoint = copy_system.extract_basepoint()
                return Parametrization(basepoint, direction_vectors)
                #return "Infinitely many solutions."
        return saved_solutions
    
    # def paramaterize():
    
    def leftmost_one(self, row):
        for i in range(0, self.planes[0].dimension):
            if MyDecimal(Decimal(self.planes[row][i]) - Decimal(1.0)).is_near_zero():
                return i
        return -1
    
    def compute_triangular_form(self):
        system = deepcopy(self)
        
        num_equations = len(self.planes)
        num_variables = self.planes[0].dimension
        current_column = 0
        
        for current_row in range(num_equations):
            current_column = current_row
            first_nonzero = True
            while current_column < num_variables:
                current_coefficient = system[current_row][current_column]
                if MyDecimal(current_coefficient).is_near_zero():
                    # move the first nonzero term up high
                    if first_nonzero: # if all preceding values are 0
                        if system.swap_with_highest_nonzero_row(current_row, current_column): #if a swappable row exists
                            # set column below pivot to zeroes
                            system.clear_below(current_row, current_column)   
                            if current_column == num_variables - 1 and self.planes[current_row][current_column] == 0:
                                current_column += 1
                        else:
                            current_column += 1
                    else:
                        current_column += 1
                else:
                    if first_nonzero: # if all the prior columns in this row are zeroes
                        # clear the first valued column's values in other rows
                        system.clear_below(current_row, current_column)
                        first_nonzero = False
                    current_column+=1
                    continue
        # convert the redundant equations to all zeroes
        if num_equations > num_variables:
            for i in range(num_variables, num_equations):
                system[i] = Plane()
        return system
    
    def compute_rref(self):
        system = self.compute_triangular_form()
        system.extract_basepoint()
        system.extract_direction_vectors()
        
        for current_row in range(len(system.planes)):
            pivot_found = False
            for current_col in range(system.planes[0].dimension):
                if not MyDecimal(system.planes[current_row][current_col]).is_near_zero():
                    if not pivot_found:
                        pivot_found = True
                        system.clear_above(current_row, current_col)
                        system.set_pivot_to_one(current_row, current_col)
        return system
    
    def set_pivot_to_one(self, current_row, current_col):
        divide_ratio = 1
        for i in range (current_col, self.planes[0].dimension+1):
            if i == current_col:
                divide_ratio = self.planes[current_row][current_col]
            self.planes[current_row][i] /= divide_ratio
    
    def swap_with_highest_nonzero_row(self, row, column): #swap row with the highest row that's nonzero in the same column
        changed = False
        for i in range(row+1, len(self.planes)):
            if not MyDecimal(self.planes[i][column]).is_near_zero():
                self.swap_rows(row, i)
                changed = True
                break
        return changed
    
    def clear_below(self, row, column): # set to 0 below a pivot
        for i in range(row+1, len(self.planes)):
            if not MyDecimal(self.planes[i][column]).is_near_zero():
                cancel_ratio = -(self.planes[i][column] / self.planes[row][column])
                self.add_multiple_times_row_to_row(cancel_ratio, row, i)
    
    def clear_above(self, row, column): # set to 0 above a pivot
        for i in range(row):
            if not MyDecimal(self.planes[i][column]).is_near_zero():
                coefficient = -(self.planes[i][column] / self.planes[row][column])
                self.add_multiple_times_row_to_row(coefficient, row, i) #cancel the value directly above pivot
            
        
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

    def extract_basepoint(self): #find the coefficient of each first pivot variable in each row
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coords = [0] * num_variables

        for i, plane in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            basepoint_coords[pivot_var] = plane.constant_term
    
        return Vector(basepoint_coords)

    def extract_direction_vectors(self): #find the coefficient of each column 2, 3, etc variable
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set(range(num_variables)) - set(pivot_indices)

        direction_vectors = []

        for free_var in free_variable_indices:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1 # a free variable can only be equal to itself
            for i, plane in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -plane.normal_vector[free_var] #take coefficient of free variable for a particular equation, on the other side

            direction_vectors.append(Vector(vector_coords))
        return direction_vectors
    
class Parametrization(object):

    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM = "Error: The basepoint and direction vectors are not in the same dimension."

    def __init__(self, basepoint, direction_vectors):

        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension
        '''print self.basepoint
        for i in range(len(self.direction_vectors)):
            print self.direction_vectors[i]'''

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM)
    
    
    def __str__(self): 
        
        #derive the parameters
        # x_1 = first value of each vector. basepoint value listed is a constant, second is in terms of t_1, third in t_2, and so on
        # x_2 = second value of each vector
        # x_3 = third value of each vector
        
        output = ''
        for coord in range(self.dimension):
            output += 'x_{} = {} '.format(coord + 1, round(self.basepoint[coord], 3))
            for free_var, vector in enumerate(self.direction_vectors):
                output += '+ {} t_{}'.format(round(vector[coord], 3), free_var + 1) 
            output += '\n'
        return output

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