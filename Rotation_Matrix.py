import numpy as np


class Rotate:
    def __init__(self):
        pass

    def rotateZ(self, degree, position = [0, 0]):
        radian = degree * np.pi / 180.0
        matrix = np.array([
            [np.cos(radian), -np.sin(radian), 0.0, position[0]],
            [np.sin(radian), np.cos(radian), 0.0, position[1]],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ], dtype=np.float32)
        return matrix

    def rotateY(self,degree,position = [0,0]):
        radian = degree*np.pi/180.0
        matrix = np.array([
            [np.cos(radian),0.0,np.sin(radian),position[0]],
            [0.0,1.0,0.0,position[1]],
            [-np.sin(radian),0.0,np.cos(radian),0.0],
            [0.0,0.0,0.0,1.0]
        ])
        return matrix

    def rotateY1(self,degree):
        radian = degree*np.pi/180.0
        matrix = np.array([
            [np.cos(radian),0.0,np.sin(radian)],
            [0.0,1.0,0.0],
            [-np.sin(radian),0.0,np.cos(radian)]
        ])
        return matrix

    def rotateX(self,degree,position = [0,0]):
        radian = degree*np.pi/180.0
        matrix = np.array([
            [1.0,0.0,0.0,position[0]],
            [0.0,np.cos(radian),-np.sin(radian),position[1]],
            [0.0,np.sin(radian),np.cos(radian),0.0],
            [0.0,0.0,0.0,1.0]
        ])
        return matrix
    
    def rotateX1(self,degree):
        radian = degree*np.pi/180.0
        matrix = np.array([
            [1.0,0.0,0.0],
            [0.0,np.cos(radian),-np.sin(radian)],
            [0.0,np.sin(radian),np.cos(radian)]
        ])
        return matrix
    
    def translate(self,position):
        matrix = np.array([[1,0,0,[position[0]],
                           [0,1,0,position[1]]],
                           [0,0,1,position[2]]])
        return matrix


    def rotateXY(self,degree,position= [0,0]):
        radian = degree*np.pi/180.0
        matrix = np.array([
            [np.cos(radian),0.0,np.sin(radian),position[0]],
            [0.0,np.cos(radian),-np.sin(radian),position[1]],
            [-np.sin(radian),np.sin(radian),np.cos(radian),0.0],
            [0.0,0.0,0.0,1.0]
        ])
        return matrix

def getUnitVector(x,y,z):
    l = ((x**2) + (y**2) + (z**2))**0.5
    return (x/l, y/l, z/l)


def rotateY(degree):
    radian = degree*np.pi/180.0
    matrix = np.array([
        [np.cos(radian),0.0,np.sin(radian)],
        [0.0,1.0,0.0],
        [-np.sin(radian),0.0,np.cos(radian)]
    ])
    return matrix

def rotateX(degree):
        radian = degree*np.pi/180.0
        matrix = np.array([
            [1.0,0.0,0.0],
            [0.0,np.cos(radian),-np.sin(radian)],
            [0.0,np.sin(radian),np.cos(radian)]
        ])
        return matrix

def rotateZ(degree):
        radian = degree * np.pi / 180.0
        matrix = np.array([
            [np.cos(radian), -np.sin(radian), 0.0,],
            [np.sin(radian), np.cos(radian), 0.0,],
            [0.0, 0.0, 1.0,]
        ], dtype=np.float32)
        return matrix


