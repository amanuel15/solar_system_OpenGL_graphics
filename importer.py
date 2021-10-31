from PIL import Image
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
from circle_vertex import *
from Rotation_Matrix import *
from sphere_vertex import *
from sphere_vertexes2 import *
from sphere_coordinates_testing import *
pygame.mixer.init()

def load_circle():
    x = vertex_circle()
    return x

def load_sphere():
    x = sphere_vertexes()
    return x


def load_sphere2():
    x = sphere_vertexes2()
    return x


def load_skymap():
    vertexes = [
        [5, 5, 5, 1, 1, 1, 1.0, 1.0],
        [5, -5, 5, 1, 1, 1, 1.0, 0.0],
        [-5, -5, 5, 1, 1, 1, 0.0, 0.0],
        [-5, 5, 5, 1, 1, 1, 0.0, 1.0],

        [5, -5, -5, 1, 1, 1, 1.0, 0.0],
        [5, 5, -5, 1, 1, 1, 1.0, 1.0],
        [5, 5, 5, 1, 1, 1, 0.0, 1.0],
        [5, -5, 5, 1, 1, 1, 0.0, 0.0],

        [5, 5, -5, 1, 1, 1, 1.0, 1.0],
        [5, -5, -5, 1, 1, 1, 1.0, 0.0],
        [-5, -5, -5, 1, 1, 1, 0.0, 0.0],
        [-5, 5, -5, 1, 1, 1, 0.0, 1.0],
        
        [-5, -5, -5, 1, 1, 1, 0.0, 0.0],
        [-5, 5, -5, 1, 1, 1, 0.0, 1.0],
        [-5, 5, 5, 1, 1, 1, 1.0, 1.0],
        [-5, -5, 5, 1, 1, 1, 1.0, 0.0],

        [5, 5, 5, 1, 1, 1, 1.0, 0.0],
        [5, 5, -5, 1, 1, 1, 1.0, 1.0],
        [-5, 5, -5, 1, 1, 1, 0.0, 1.0],
        [-5, 5, 5, 1, 1, 1, 0.0, 0.0],

        [5, -5, 5, 1, 1, 1, 1.0, 1.0],
        [5, -5, -5, 1, 1, 1, 1.0, 0.0],
        [-5, -5, -5, 1, 1, 1, 0.0, 0.0],
        [-5, -5, 5, 1, 1, 1, 0.0, 1.0]
        ]
    return vertexes
