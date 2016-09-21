from vector import Vector

#question 1
vector1 = Vector([7.887, 4.138])
vector2 = Vector([-8.802, 6.776])
print vector1.dot_product(vector2)

#question 2
vector3 = Vector([-5.955, -4.904, -1.874])
vector4 = Vector([-4.496, -8.755, 7.103])
print vector3.dot_product(vector4)

#question 3
vector5 = Vector([3.183, -7.627])
vector6 = Vector([-2.668, 5.319])
print vector5.angle(vector6, True)

#question 4
vector7 = Vector([7.35, 0.221, 5.188])
vector8 = Vector([2.751, 8.259, 3.985])
print vector7.angle(vector8, False)