'''
Author: Julio Cesar Ramirez Ceballos
Institute: ESTIA
Licence: MIT

Description:
This functions are used in the main script to generate the data to
train the robot.

'''

from math import sin, cos, sqrt
import numpy as np
from sympy import *

def rad2deg(rad):
    deg = rad*180/np.pi
    return deg

def deg2rad(deg):
    rad = deg*np.pi/180
    return rad

def rotx(a):
    m = [[1,0,0,0],[0,cos(a),-sin(a),0],[0,sin(a),cos(a),0],[0,0,0,1]];
    m = np.array(m)
    return m

def roty(a):
    m = [[cos(a),0,sin(a),0],[0,1,0,0],[-sin(a),0,cos(a),0],[0,0,0,1]];
    m = np.array(m)
    return m

def rotz(a):
    m = [[cos(a),-sin(a),0,0],[sin(a),cos(a),0,0],[0,0,1,0],[0,0,0,1]];
    m = np.array(m)
    return m

def transl(x, y, z):
    m = [[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]];
    m = np.array(m)
    return m

def dhm(alpha, d, theta, r):
    m = [[cos(theta), -sin(theta), 0, d],
         [cos(alpha)*sin(theta), cos(alpha)*cos(theta), -sin(alpha), -r*sin(alpha)],
         [sin(alpha)*sin(theta), sin(alpha)*cos(theta), cos(alpha), r*cos(alpha)],
         [0, 0, 0, 1]]
    m = np.array(m)
    return m

def quat(R):
    # only gets the rotation matrix from the Tkfm matrix
    sx = R[0,0]; nx = R[0,1]; ax = R[0,2];
    sy = R[1,0]; ny = R[1,1]; ay = R[1,2];
    sz = R[2,0]; nz = R[2,1]; az = R[2,2];

    a = sqrt(sx + ny + az + 1)/2
    rx = (nz - ay)/(4*a)
    ry = (ax - sz)/(4*a)
    rz = (sy - nx)/(4*a)
    return a,rx,ry,rz
