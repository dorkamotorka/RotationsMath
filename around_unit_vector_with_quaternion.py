#!/usr/bin/python
from math import sin, cos

M_PI = 3.14159

def rotation_around_unit_vector_to_quaternion(unit_vector, angle):
    q0 = cos(angle/2)
    q1 = sin(angle/2) * unit_vector[0]
    q2 = sin(angle/2) * unit_vector[1]
    q3 = sin(angle/2) * unit_vector[2]

    return q0, q1, q2, q3

unit_vector = [0, 0, 1]
angle = M_PI
print(rotation_around_unit_vector_to_quaternion(unit_vector, angle))
