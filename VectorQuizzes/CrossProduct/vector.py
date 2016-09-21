import math
import sys

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def add(self, v):
        newCoordinates = [0] * self.dimension
        if self.dimension == v.dimension:
            for i in range(self.dimension):
                newCoordinates[i] = self.coordinates[i] + v.coordinates[i]
            return Vector(newCoordinates)
        else:
            return "The vectors have different dimensions, and thus cannot be added together."

    def subtract(self, v):
        newCoordinates = [0] * self.dimension
        if self.dimension == v.dimension:
            for i in range(self.dimension):
                newCoordinates[i] = self.coordinates[i] - v.coordinates[i]
            return Vector(newCoordinates)
        else:
            return "The vectors have different dimensions, and thus cannot be subtracted."
    
    def scalar_multiply(self, scalar):
        newCoordinates = [0] * self.dimension
        for i in range(self.dimension):
            newCoordinates[i] = self.coordinates[i] * scalar
        return Vector(newCoordinates)
    
    def magnitude(self):
        magnitude = 0
        for i in range(self.dimension):
            magnitude += (self.coordinates[i] * self.coordinates[i])
        return math.sqrt(magnitude)
        
    def unit_size(self):
        newCoordinates = [0] * self.dimension
        magnitude = self.magnitude()
        for i in range(self.dimension):
            newCoordinates[i] = (self.coordinates[i] / magnitude)
        return Vector(newCoordinates)
    
    def dot_product(self, v):
        dotProduct = 0
        for i in range(self.dimension):
            dotProduct += self.coordinates[i] * v.coordinates[i]
        return dotProduct
    
    def angle(self, v, radians):
        dotProduct = self.dot_product(v)
        magnitudeProduct = self.magnitude() * v.magnitude()
        if magnitudeProduct == 0:
                return 0
        elif radians:
            return math.acos(dotProduct/magnitudeProduct)
        else:
            return math.degrees(math.acos(dotProduct/magnitudeProduct))
    
    def parallel_to(self, v): #angle is close enough to zero, adjusting for rounding error
        angle = self.angle(v, False)
        print angle
        return ((angle < 100*sys.float_info.epsilon and angle > -100*sys.float_info.epsilon) or (angle-180 < 100*sys.float_info.epsilon and angle-180 > -100*sys.float_info.epsilon))
    
    def orthogonal_to(self, v): #dot product is close enough to zero, adjusting for rounding error
        dotProduct = self.dot_product(v)        
        print dotProduct
        return dotProduct < 100*sys.float_info.epsilon and dotProduct > -100*sys.float_info.epsilon
    
    def projection_on(self, basis): #the parallel component of v, extracted from self's component in that direction. 
        unitVector = basis.unit_size() #unit vector in basis direction
        vParallelLength = self.dot_product(unitVector) #length of Vparallel is the basis unit vector dot V
        return unitVector.scalar_multiply(vParallelLength) #VParallel is the basis unit vector times the length of Vparallel
     
    def perpendicular_component_of(self, basis): #the perpendicular component of v, derived from self's component in its direction
        return self.subtract(self.projection_on(basis)) #Vperpendicular is V minus Vparallel
    
    def cross_product(self, v):
        if self.dimension == 3 and v.dimension == 3:
            newCoordinates = [0]*3
            newCoordinates[0] = (self.coordinates[1] * v.coordinates[2]) - (self.coordinates[2] * v.coordinates[1])
            newCoordinates[1] = -(self.coordinates[0] * v.coordinates[2]) + self.coordinates[2] * v.coordinates[0]
            newCoordinates[2] = (self.coordinates[0] * v.coordinates[1]) - (self.coordinates[1] * v.coordinates[0])
            return Vector(newCoordinates)
        else:
            return "Error: the cross product operation is only possible between vectors of three dimensions each."
    
    def parallelogram_area(self, v):
        return self.cross_product(v).magnitude()
    
    def triangle_area(self, v):
        return 0.5 * self.parallelogram_area(v)
    
    #cross product: orthogonal to both vectors. Length: magnitudes multiplied, times sin(theta)
    #if vectors parallel, it returns 0. If one vector is the zero vector, also returns 0
    # v cross w = -(w cross v)
    #treat v as the base. the line from v to the end of w is the height. thus, height = magnitude of w times sin(theta)
    #cross product formula: y1z2 - y2z1 - x1z2 + x2z1 + x1y2 - x2y1
    #area of parallelogram formed by two vectors: magnitude of the cross product
    #area of triangle spanned by two vectors: 0.5 * magnitude of the cross product