import math

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
        if radians:
            return math.acos(dotProduct/magnitudeProduct)
        else:
            return math.degrees(math.acos(dotProduct/magnitudeProduct))
        
    # angle between: arccos(dot product of values / product of magnitudes, OR product of the unit sizes). Derived from law of cosines
    # 0 angle: same direction. 0 product: orthogonal