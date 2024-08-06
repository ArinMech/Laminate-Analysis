# Importing necessary libraries
from sympy import symbols, Matrix, pretty_print
from math import cos, sin, pi, degrees
import random
# PW = Plain Weave and UD = Uni Directional
E1PW = 6.0263e+10; #Pa, Experimentally Gathered
E2PW = 6.0263e+10; #Pa, estimate
nu12PW = 0.04; #Room Temperature Ambient, Data sheet
G12PW = 4.21e+9; #Pa, Data sheet
t_PW = .2032; #mm

E1UD = 1.63e+11; #Pa, Experimentally Gathered
E2UD = 8.41e+9; #Pa, estimate
nu12UD = 0.31; #Room Temperature Ambient, Data sheet
nu21UD = 0.01599 #Calculated
G12UD = 4.23e+9; #Pa, Data sheet
t_UD = .152; #mm

Min_Plies = 2
Max_Plies = 6

# Equal number of 0 and 90 plies
# Defining each ply's class
class uni_0():
    name = "Uni0"
    E1 = E1UD
    E2 = E2UD
    nu12 = nu12UD
    nu21 = nu21UD
    G12 = G12UD
    t = t_UD
    theta = 0 # Default
    m = cos(theta*pi/180)
    n = sin(theta*pi/180)
    Q = Matrix([[E1/(1-nu12*nu21), (nu21*E1)/(1-nu12*nu21), 0], [(nu21*E1)/(1-nu12*nu21), E2/(1-nu12*nu21), 0], [0, 0, G12]])
    T = Matrix([[m**4, n**4, 2*m**2*n**2, 4*m**2*n**2], [n**4, m**4, 2*m**2*n**2, 4*m**2*n**2], [m**2*n**2, m**2*n**2, m**4 + n**4, -4*m**2*n**2], [m**3*n, -m*n**3, -m*n*(m**2 - n**2), -2*m*n*(m**2-n**2)], [m*n**3, -m**3*n, m*n*(m**2 - n**2), 2*m*n*(m**2 - n**2)], [m**2*n**2, m**2*n**2, -2*m**2*n**2, (m**2 - n**2)**2]])
    Q_new = T*Matrix([[Q[0]], [Q[4]], [Q[3]], [Q[8]]])
    Q_T = Matrix([[Q_new[0], Q_new[2], Q_new[3]], [Q_new[2], Q_new[1], Q_new[4]], [Q_new[3], Q_new[4], Q_new[5]]])
uni_ply_0 = uni_0()

class uni_90():
    name = "Uni90"
    E1 = E1UD
    E2 = E2UD
    nu12 = nu12UD
    nu21 = nu21UD
    G12 = G12UD
    t = t_UD
    theta = 90 # Default
    m = cos(theta*pi/180)
    n = sin(theta*pi/180)
    Q = Matrix([[E1/(1-nu12*nu21), (nu21*E1)/(1-nu12*nu21), 0], [(nu21*E1)/(1-nu12*nu21), E2/(1-nu12*nu21), 0], [0, 0, G12]])
    T = Matrix([[m**4, n**4, 2*m**2*n**2, 4*m**2*n**2], [n**4, m**4, 2*m**2*n**2, 4*m**2*n**2], [m**2*n**2, m**2*n**2, m**4 + n**4, -4*m**2*n**2], [m**3*n, -m*n**3, -m*n*(m**2 - n**2), -2*m*n*(m**2-n**2)], [m*n**3, -m**3*n, m*n*(m**2 - n**2), 2*m*n*(m**2 - n**2)], [m**2*n**2, m**2*n**2, -2*m**2*n**2, (m**2 - n**2)**2]])
    Q_new = T*Matrix([[Q[0]], [Q[4]], [Q[3]], [Q[8]]])
    Q_T = Matrix([[Q_new[0], Q_new[2], Q_new[3]], [Q_new[2], Q_new[1], Q_new[4]], [Q_new[3], Q_new[4], Q_new[5]]])
uni_ply_90 = uni_90()

class plain_0():
    name = "PW0"
    E1 = E1PW
    E2 = E2PW
    nu12 = nu12PW
    G12 = G12PW
    t = t_PW
    theta = 0 # Default
    m = cos(theta*pi/180)
    n = sin(theta*pi/180)
    Q = Matrix([[E1/(1-nu12**2), (nu12*E1)/(1-nu12**2), 0], [(nu12*E1)/(1-nu12**2), E2/(1-nu12**2), 0], [0, 0, G12]])
    T = Matrix([[m**4, n**4, 2*m**2*n**2, 4*m**2*n**2], [n**4, m**4, 2*m**2*n**2, 4*m**2*n**2], [m**2*n**2, m**2*n**2, m**4 + n**4, -4*m**2*n**2], [m**3*n, -m*n**3, -m*n*(m**2 - n**2), -2*m*n*(m**2-n**2)], [m*n**3, -m**3*n, m*n*(m**2 - n**2), 2*m*n*(m**2 - n**2)], [m**2*n**2, m**2*n**2, -2*m**2*n**2, (m**2 - n**2)**2]])
    Q_new = T*Matrix([[Q[0]], [Q[4]], [Q[3]], [Q[8]]])
    Q_T = Matrix([[Q_new[0], Q_new[2], Q_new[3]], [Q_new[2], Q_new[1], Q_new[4]], [Q_new[3], Q_new[4], Q_new[5]]])
plain_weave_0 = plain_0()
plain_weave_0.theta = 0

class plain_45():
    name = "PW45"
    E1 = E1PW
    E2 = E2PW
    nu12 = nu12PW
    G12 = G12PW
    t = t_PW
    theta = 45 # Default
    m = cos(theta*pi/180)
    n = sin(theta*pi/180)
    Q = Matrix([[E1/(1-nu12**2), (nu12*E1)/(1-nu12**2), 0], [(nu12*E1)/(1-nu12**2), E2/(1-nu12**2), 0], [0, 0, G12]])
    T = Matrix([[m**4, n**4, 2*m**2*n**2, 4*m**2*n**2], [n**4, m**4, 2*m**2*n**2, 4*m**2*n**2], [m**2*n**2, m**2*n**2, m**4 + n**4, -4*m**2*n**2], [m**3*n, -m*n**3, -m*n*(m**2 - n**2), -2*m*n*(m**2-n**2)], [m*n**3, -m**3*n, m*n*(m**2 - n**2), 2*m*n*(m**2 - n**2)], [m**2*n**2, m**2*n**2, -2*m**2*n**2, (m**2 - n**2)**2]])
    Q_new = T*Matrix([[Q[0]], [Q[4]], [Q[3]], [Q[8]]])
    Q_T = Matrix([[Q_new[0], Q_new[2], Q_new[3]], [Q_new[2], Q_new[1], Q_new[4]], [Q_new[3], Q_new[4], Q_new[5]]])
plain_weave_45 = plain_45()

class plain_90():
    name = "PW90"
    E1 = E1PW
    E2 = E2PW
    nu12 = nu12PW
    G12 = G12PW
    t = t_PW
    theta = 90 # Default
    m = cos(theta*pi/180)
    n = sin(theta*pi/180)
    Q = Matrix([[E1/(1-nu12**2), (nu12*E1)/(1-nu12**2), 0], [(nu12*E1)/(1-nu12**2), E2/(1-nu12**2), 0], [0, 0, G12]])
    T = Matrix([[m**4, n**4, 2*m**2*n**2, 4*m**2*n**2], [n**4, m**4, 2*m**2*n**2, 4*m**2*n**2], [m**2*n**2, m**2*n**2, m**4 + n**4, -4*m**2*n**2], [m**3*n, -m*n**3, -m*n*(m**2 - n**2), -2*m*n*(m**2-n**2)], [m*n**3, -m**3*n, m*n*(m**2 - n**2), 2*m*n*(m**2 - n**2)], [m**2*n**2, m**2*n**2, -2*m**2*n**2, (m**2 - n**2)**2]])
    Q_new = T*Matrix([[Q[0]], [Q[4]], [Q[3]], [Q[8]]])
    Q_T = Matrix([[Q_new[0], Q_new[2], Q_new[3]], [Q_new[2], Q_new[1], Q_new[4]], [Q_new[3], Q_new[4], Q_new[5]]])
plain_weave_90 = plain_90()

import itertools

def generate_combinations_with_replacement(obj_names, min_size=2, max_size=6):
    # List to store all possible combinations with replacement
    all_combinations = []

    # Generate combinations with replacement for sizes ranging from min_size to max_size
    for r in range(min_size, max_size + 1):
        combinations = (itertools.product(obj_names, repeat=r))
        all_combinations.extend(combinations)

    return all_combinations

# Example usage
obj_names = [uni_ply_0.name, plain_weave_0.name, plain_weave_45.name, plain_weave_90.name, uni_ply_90.name]

# Generate all possible combinations with replacement
all_combinations = generate_combinations_with_replacement(obj_names)

# Print all possible combinations
for combo in all_combinations:
    print(combo)

