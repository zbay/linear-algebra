from vector import Vector

#question 1
vector1 = Vector([8.462, 7.893, -8.187])
vector2 = Vector([6.984, -5.975, 4.778])
print vector1.cross_product(vector2)

#question 2
vector3 = Vector([-8.987, -9.838, 5.031])
vector4 = Vector([-4.268, -1.861, -8.866])
print vector3.parallelogram_area(vector4)

#question 3
vector5 = Vector([1.5, 9.547, 3.691])
vector6 = Vector([-6.007, 0.124, 5.772])
print vector5.triangle_area(vector6)