#!/usr/bin/python

def quaternion_to_rotation_matrix(q0, q1, q2, q3):
    a11 = q0**2 + q1**2 - q2**2 - q3**2
    a12 = 2 * (q1*q2 - q0*q3)
    a13 = 2 * (q1*q3 + q0*q2)
    a21 = 2 * (q1*q2 + q0*q3)
    a22 = q0**2 - q1**2 + q2**2 - q3**2
    a23 = 2 * (q2*q3 - q0*q1)
    a31 = 2 * (q1*q3 - q0*q2)
    a32 = 2 * (q2*q3 + q0*q1)
    a33 = q0**2 - q1**2 - q2**2 + q3**2
    return [[a11, a12, a13],
            [a21, a22, a23],
            [a31, a32, a33]]
    
quat = [1, 0, 0, 0]
print(quaternion_to_rotation_matrix(*quat))
