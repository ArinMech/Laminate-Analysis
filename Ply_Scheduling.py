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

E3UD = 1.63e+11; #Pa, Experimentally Gathered
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
# Generating random combinations of Objects
import itertools

def generate_combinations_with_replacement(obj_names, min_size=2, max_size=6):
    # List to store all possible combinations with replacement
    all_combinations_objects = []

    # Generate combinations with replacement for sizes ranging from min_size to max_size
    for r in range(min_size, max_size + 1):
        combinations = itertools.product(obj_names, repeat=r)
        all_combinations_objects.extend(combinations)

    return all_combinations_objects

# Example usage
obj_names = [uni_ply_0, plain_weave_0, plain_weave_45, plain_weave_90, uni_ply_90]

# Generate all possible combinations with replacement
all_combinations_objects = generate_combinations_with_replacement(obj_names)

# Code for A Matrix
def A_Matrix(schedule):
    sum = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for i in schedule:
        if "PW" in i.name:
            t = 0.2032
        else:
            t = 0.152
        sum += t*i.Q_T
    return sum

A_Matrix_List = []
for combo in all_combinations_objects:
    pretty_print(A_Matrix(combo))
    A_Matrix_List.append(A_Matrix(combo))

#Filteration of the plies according to FSAE rules
filter = []
for i in all_combinations_objects:
    count0 = 0
    count90 = 0
    for j in i:
        if "PW" in j.name:
            if "PW0" == j.name or "PW90" == j.name:
                count0 += 1
                count90 += 1
        else:
            if "Uni0" == j.name:
                count0 += 1
            elif "Uni90" == j.name:
                count90 += 1
    if count90 == count0 / 2:
        filter.append(i)
print(filter)

# Viewing names of filtered objects
name_list = []
for i in filter:
    list_sample = []
    for j in i:
        list_sample.append(j.name)
    name_list.append(list_sample)
    print(list_sample)

A_Matrix_List = []
for combo in filter:
    pretty_print(A_Matrix(combo))
    A_Matrix_List.append(A_Matrix(combo))

A_Inverse = []
for i in A_Matrix_List:
    A_Inverse.append(i.inv())

thickness = []
for i in filter:
    sum = 0
    for j in i:
        sum += j.t
    thickness.append(sum)
for i in thickness:
    print(i)

E_Matrix = []
count = 0
for i in A_Inverse:
    E_Matrix.append(1/(i[0]*thickness[count]))
    count += 1
combined = list(zip(E_Matrix, name_list))
sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
sorted_E, sorted_name = zip(*sorted_combined)
sorted_E = list(sorted_E)
sorted_name = list(sorted_name)
for i in range(1025):
    print(sorted_E[i], sorted_name[i])

def sym(list):
    if len(list) % 2 == 0:
        list_half = list[0:int(len(list)/2)]
        list_sec_half = list[int(len(list)/2):len(list)]
        list_half.reverse()
        if list_sec_half == list_half:
            return True
        else:
            return False
    else:
        element = len(list) / 2 - 0.5
        list_half = list[0:int(element)]
        list_sec_half = list[int(element + 1):len(list)]
        if list_sec_half == list_half[::-1]:
            return True
        else:
            return False

# Apply the condition and filter both lists accordingly
filtered_list1 = []
filtered_list2 = []

for num, word in zip(sorted_E, sorted_name):
    if sym(word):
        filtered_list1.append(num)
        filtered_list2.append(word)

for i in range(31):
    print(filtered_list1[i], filtered_list2[i])


