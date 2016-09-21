from vector import Vector

#question 1
vector1 = Vector([-7.579, -7.88])
vector2 = Vector([22.737, 23.64])
print vector1.parallel_to(vector2)
print vector1.orthogonal_to(vector2)

#question 2
vector3 = Vector([-2.029, 9.97, 4.172])
vector4 = Vector([-9.231, -6.639, -7.245])
print vector3.parallel_to(vector4)
print vector3.orthogonal_to(vector4)

#question 3
vector5 = Vector([-2.328, -7.284, -1.214])
vector6 = Vector([-1.821, 1.072, -2.94])
print vector5.parallel_to(vector6)
print vector5.orthogonal_to(vector6)

#question 4
vector7 = Vector([2.118, 4.827])
vector8 = Vector([0, 0])
print vector7.parallel_to(vector8)
print vector7.orthogonal_to(vector8)