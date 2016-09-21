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
        