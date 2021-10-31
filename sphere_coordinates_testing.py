import os
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
import random
import threading
from math import *
from Rotation_Matrix import *


def rotate(initial_coordinates, frame_coordinates, degree):
    rotated_coordinates = [0, 0, 0]
    rotated_coordinates[0] = frame_coordinates[0] + (
            (initial_coordinates[0] - frame_coordinates[0]) * cos(radians(degree))) - (
                                     (initial_coordinates[1] - frame_coordinates[1]) * sin(radians(degree)))
    rotated_coordinates[1] = frame_coordinates[1] + (
            (initial_coordinates[0] - frame_coordinates[0]) * sin(radians(degree))) + (
                                     (initial_coordinates[1] - frame_coordinates[1]) * cos(radians(degree)))
    return rotated_coordinates


def generate_Circle(radius, angle):
    Triangle_Verticies = []
    frame_coordinates = [0.0, 0.0]
    iteration = 360 / angle
    for i in range(int(iteration) + 1):
        verticies = rotate(radius, frame_coordinates, i * angle)
        Triangle_Verticies.append(verticies)
    return Triangle_Verticies


def multiply3by3_matix(a, b):
    final = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=np.float32)
    final[0][0] = (a[0][0] * b[0][0]) + (a[0][1] * b[1][0]) + (a[0][2] * b[2][0])
    final[0][1] = (a[0][0] * b[0][1]) + (a[0][1] * b[1][1]) + (a[0][2] * b[2][1])
    final[0][2] = (a[0][0] * b[0][2]) + (a[0][1] * b[1][2]) + (a[0][2] * b[2][2])

    final[1][0] = (a[1][0] * b[0][0]) + (a[1][1] * b[1][0]) + (a[1][2] * b[2][0])
    final[1][1] = (a[1][0] * b[0][1]) + (a[1][1] * b[1][1]) + (a[1][2] * b[2][1])
    final[1][2] = (a[1][0] * b[0][2]) + (a[1][1] * b[1][2]) + (a[1][2] * b[2][2])

    final[2][0] = (a[2][0] * b[0][0]) + (a[2][1] * b[1][0]) + (a[2][2] * b[2][0])
    final[2][1] = (a[2][0] * b[0][1]) + (a[2][1] * b[1][1]) + (a[2][2] * b[2][1])
    final[2][2] = (a[2][0] * b[0][2]) + (a[2][1] * b[1][2]) + (a[2][2] * b[2][2])

    return final


def multiply4by4_martix(a, b):
    final = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=np.float32)
    final[0][0] = (a[0][0] * b[0][0]) + (a[0][1] * b[1][0]) + (a[0][2] * b[2][0]) + (a[0][3] * b[3][0])
    final[0][1] = (a[0][0] * b[0][1]) + (a[0][1] * b[1][1]) + (a[0][2] * b[2][1]) + (a[0][3] * b[3][1])
    final[0][2] = (a[0][0] * b[0][2]) + (a[0][1] * b[1][2]) + (a[0][2] * b[2][2]) + (a[0][3] * b[3][2])
    final[0][3] = (a[0][0] * b[0][3]) + (a[0][1] * b[1][3]) + (a[0][2] * b[2][3]) + (a[0][3] * b[3][3])

    final[1][0] = (a[1][0] * b[0][0]) + (a[1][1] * b[1][0]) + (a[1][2] * b[2][0]) + (a[1][3] * b[3][0])
    final[1][1] = (a[1][0] * b[0][1]) + (a[1][1] * b[1][1]) + (a[1][2] * b[2][1]) + (a[1][3] * b[3][1])
    final[1][2] = (a[1][0] * b[0][2]) + (a[1][1] * b[1][2]) + (a[1][2] * b[2][2]) + (a[1][3] * b[3][2])
    final[1][3] = (a[1][0] * b[0][3]) + (a[1][1] * b[1][3]) + (a[1][2] * b[2][3]) + (a[1][3] * b[3][3])

    final[2][0] = (a[2][0] * b[0][0]) + (a[2][1] * b[1][0]) + (a[2][2] * b[2][0]) + (a[2][3] * b[3][0])
    final[2][1] = (a[2][0] * b[0][1]) + (a[2][1] * b[1][1]) + (a[2][2] * b[2][1]) + (a[2][3] * b[3][1])
    final[2][2] = (a[2][0] * b[0][2]) + (a[2][1] * b[1][2]) + (a[2][2] * b[2][2]) + (a[2][3] * b[3][2])
    final[2][3] = (a[2][0] * b[0][3]) + (a[2][1] * b[1][3]) + (a[2][2] * b[2][3]) + (a[2][3] * b[3][3])

    final[3][0] = (a[3][0] * b[0][0]) + (a[3][1] * b[1][0]) + (a[3][2] * b[2][0]) + (a[3][3] * b[3][0])
    final[3][1] = (a[3][0] * b[0][1]) + (a[3][1] * b[1][1]) + (a[3][2] * b[2][1]) + (a[3][3] * b[3][1])
    final[3][2] = (a[3][0] * b[0][2]) + (a[3][1] * b[1][2]) + (a[3][2] * b[2][2]) + (a[3][3] * b[3][2])
    final[3][3] = (a[3][0] * b[0][3]) + (a[3][1] * b[1][3]) + (a[3][2] * b[2][3]) + (a[3][3] * b[3][3])
    return final


'''
for i in range(4):
    ist(i,4,final[i],a,b)

'''


def ist(initial, final, matrix, a, b):
    for i in range(final):
        matrix[i] = (a[initial][0] * b[0][i]) + (a[initial][1] * b[1][i]) + (a[initial][2] * b[2][i]) + (
                    a[initial][3] * b[3][i])


def multiply4by1_matrix(a, b):
    final = [0, 0, 0, 0]
    final[0] = (a[0][0] * b[0]) + (a[0][1] * b[1]) + (a[0][2] * b[2]) + (a[0][3] * b[3])
    final[1] = (a[1][0] * b[0]) + (a[1][1] * b[1]) + (a[1][2] * b[2]) + (a[1][3] * b[3])
    final[2] = (a[2][0] * b[0]) + (a[2][1] * b[1]) + (a[2][2] * b[2]) + (a[2][3] * b[3])
    final[3] = (a[3][0] * b[0]) + (a[3][1] * b[1]) + (a[3][2] * b[2]) + (a[3][3] * b[3])
    return final


def multiply3by1_matrix(a, b,final):
    final[0] = (a[0][0] * b[0]) + (a[0][1] * b[1]) + (a[0][2] * b[2])
    final[1] = (a[1][0] * b[0]) + (a[1][1] * b[1]) + (a[1][2] * b[2])
    final[2] = (a[2][0] * b[0]) + (a[2][1] * b[1]) + (a[2][2] * b[2])
    return final

texture_coordinates = generate_Circle([0.5, 0], 1)
for i in range(len(texture_coordinates)):
    texture_coordinates[i] = [texture_coordinates[i][0]+0.5, texture_coordinates[i][1]+0.5]
x = generate_Circle([0.2, 0, 0], 1)

m = Rotate()
z = []
# for y in range(180):
#     r = []
#     for i in x:
#         r.append(multiply4by1_matrix(m.rotateX(y),i))
#     z.append(r)
#     print(r)

# text = open("text_files/sphere_coordinates.txt", "w")
# for i in x:
#     final = [0, 0, 0,   0, 0, 1,   0,0]
#     text.write(str(multiply3by1_matrix(m.rotateX1(y), i,final)))
#     #print((str(multiply3by1_matrix(m.rotateX1(y), i,final))))
# text.write("\n")

def rotate_Celestials(position,angle):
    return multiply3by1_matrix(rotateY(angle),position,[0,0,0])










