import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os

text = open("text_files/sphere_coordinates.txt","r")
#text2 = open("text_files/sphere_coordinates1.txt","w")
#text2 = open("text_files/sphere_coordinates3.txt","w")
text2r = open("text_files/sphere_coordinates1.txt","r")

def file_parser(line):
    C_b, C, O_b = 0, 0, 0
    final_coordinates = []
    Bracket_Count = lines.count("]")
    for i in range(Bracket_Count):
        coordinates = []
        if C_b ==0:
            O_b,C_b = lines.index("["), lines.index("]")
        else:
            O_b, C_b = lines[C_b + 1:].index("[") + C_b + 1, lines[C_b + 1:].index("]") + C_b + 1

        coordinates = line[O_b:C_b+1]
        final_coordinates.append(coordinates)
    return final_coordinates


def create_coordinates(file_a,file_b):
    for i in range(len(file_a)-1):
        text2.write(file_a[i])
        text2.write(",")
        text2.write(file_a[i+1])
        text2.write(",")
        text2.write(file_b[i])
        text2.write(",")
        text2.write(file_b[i+1])
        text2.write(",")
        text2.write("\n")

# r = 0
# for lines in text2r:
#     r +=1
#     print(file_parser(lines))
# print(r)


# count = 0
# initial =[]
# final = []
# for lines in text:
#     print(file_parser(lines))
#     if count ==0:
#         initial = file_parser(lines)[:]
#     elif count ==1:
#         final= file_parser(lines)[:]
#     if count ==1:
#         create_coordinates(initial,final)
#         count = 0
#     count +=1
# print(count)

count = 0
initial = []
final = []
for lines in text:
    if count == 0:
        final = file_parser(lines)
        first = file_parser(lines)
    else:
        initial = file_parser(lines)
        create_coordinates(initial,final)
        final = initial[:]
    count +=1
count +=1
create_coordinates(initial,first)
print(count)


























