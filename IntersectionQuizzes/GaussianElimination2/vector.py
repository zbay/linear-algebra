import math
from myDecimal import MyDecimal
from decimal import Decimal

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = coordinates
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        if self.dimension != v.dimension:
            return False
        for i in range(self.dimension):
            if not MyDecimal(self.coordinates[i] - v.coordinates[i]).is_near_zero():
                return False
        return True
        
    def __iter__(self):
        return iter(self.coordinates)
    def __getitem__(self,index):
        return self.coordinates[index]
    def __setitem__(self,index,value):
        self.coordinates[index] = value
    
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
        if MyDecimal(Decimal(magnitudeProduct)).is_near_zero():
                return 0
        elif radians:
            return math.acos(dotProduct/magnitudeProduct)
        else:
            if round(dotProduct/magnitudeProduct, 6) == 1.0000:
                return 0
            else:
                return math.degrees(math.acos(dotProduct/magnitudeProduct))
    
    def parallel_to(self, v): #angle is close enough to zero, adjusting for rounding error
        angle = self.angle(v, False)
        return MyDecimal(Decimal(angle)).is_near_zero() or MyDecimal(Decimal(angle - 180)).is_near_zero()
      
    def orthogonal_to(self, v): #dot product is close enough to zero, adjusting for rounding error
        dotProduct = self.dot_product(v)        
        return MyDecimal(Decimal(dotProduct)).is_near_zero()
    
    def projection_on(self, basis): #the parallel component of v, extracted from self's component in that direction. 
        unitVector = basis.unit_size() #unit vector in basis direction
        vParallelLength = self.dot_product(unitVector) #length of Vparallel is the basis unit vector dot V
        return unitVector.scalar_multiply(vParallelLength) #VParallel is the basis unit vector times the length of Vparallel
     
    def perpendicular_component_of(self, basis): #the perpendicular component of v, derived from self's component in its direction
        return self.subtract(self.projection_on(basis)) #Vperpendicular is V minus Vparallel
    
    def cross_product(self, v): # the cross product is the determinant of the two vectors with the i, j, k components
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