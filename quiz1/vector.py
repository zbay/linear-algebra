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
