from vector import Vector

#question 1
vector1 = Vector([3.039, 1.879])
vector2 = Vector([0.825, 2.036])
print vector1.projection_on(vector2)

#question 2
vector3 = Vector([-9.88, -3.264, -8.159])
vector4 = Vector([-2.155, -9.353, -9.473])
print vector3.perpendicular_component_of(vector4)

#question 3
vector5 = Vector([3.009, -6.172, 3.692, -2.51])
vector6 = Vector([6.404, -9.144, 2.759, 8.718])
print vector5.projection_on(vector6)
print vector5.perpendicular_component_of(vector6)