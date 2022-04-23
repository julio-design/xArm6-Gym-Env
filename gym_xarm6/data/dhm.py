'''
Author: Julio Cesar Ramirez Ceballos
Institute: ESTIA
Licence: MIT

Description:
    This is the main function to get a desired position and orientation of
    the end-effector based on the DHM method.
'''

import numpy as np
import random, sys, pickle, csv
from sympy import *
from math import atan2, isclose
from gym_xarm6.data.libdhm import dhm, quat, rad2deg, deg2rad

# Use this part to get the symbolic equation and remove the q values
# ------------------------------------------------------------------
# data = []
#
# # Symbolic declaration of varibles
# q1, q2, q3, q4, q5, q6 = symbols('q1:7')
# d3, r4, d6, rf, ztool = symbols('d3'), symbols('r4'), symbols('d6'), symbols('rf'), symbols('ztool')
# d4 = symbols('d4')
# r1 = symbols('r1')
#
# # Offset of
# T2_offset = -atan2(.2845,.0535)
# T3_offset = -T2_offset
# ------------------------------------------------------------------

def get_pos_orn():
    # Joint Limints
    q1 = random.uniform(deg2rad(0), deg2rad(0)) # -360 to 360
    q2 = random.uniform(deg2rad(-118), deg2rad(120))
    q3 = random.uniform(deg2rad(-225), deg2rad(11))
    q4 = random.uniform(deg2rad(-360), deg2rad(360))
    q5 = random.uniform(deg2rad(-97), deg2rad(180))
    q6 = random.uniform(deg2rad(-360), deg2rad(360))

    q = [q1,q2,q3,q4,q5,q6]

    # DHM Method
    r1 = .267
    d3 = sqrt(.2845**2+.0535**2)
    d4 = .0775
    r4 = .3425
    d6 = .076
    rf = .097
    T01 = Matrix(dhm(0,0,q1,r1))
    T12 = Matrix(dhm(-pi/2,0,q2,0))
    T23 = Matrix(dhm(0,d3,q3,0))
    T34 = Matrix(dhm(-pi/2,d4,q4,r4))
    T45 = Matrix(dhm(pi/2,0,q5,0))
    T56 = Matrix(dhm(-pi/2,d6,q6,0))
    T6f = Matrix(dhm(0,0,0,0))
    Tftool = Matrix(dhm(0,0,0,0))
    Tw0 = Matrix(dhm(0,0,0,0))

    T06 = T01*simplify(T12*T23)*T34*T45*T56
    Tfkm = Tw0 * T06 * T6f * Tftool
    Px = Tfkm[0,3]
    Py = Tfkm[1,3]
    Pz = Tfkm[2,3]
    (a,rx,ry,rz) = quat(Tfkm)
    X = np.array([Px, Py, Pz, a, rx, ry, rz]).astype(np.float32)
    return X
