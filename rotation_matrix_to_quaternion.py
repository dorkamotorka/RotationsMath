#!/usr/bin/python
from math import sqrt

def sign(n):
    return 1 if n > 0 else -1

def rotation_matrix_to_quaternion(r):
    q0 = (1/2) * sqrt(1 + r[0][0] + r[1][1] + r[2][2])
    q1 = (1/2) * sign(r[2][1] - r[1][2]) * sqrt(1 + r[0][0] - r[1][1] - r[2][2]) 
    q2 = (1/2) * sign(r[0][2] - r[2][0]) * sqrt(1 - r[0][0] + r[1][1] - r[2][2])
    q3 = (1/2) * sign(r[1][0] - r[0][1]) * sqrt(1 - r[0][0] - r[1][1] + r[2][2])

    return q0, q1, q2, q3

rot_matrix = [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]
print(rotation_matrix_to_quaternion(rot_matrix))
