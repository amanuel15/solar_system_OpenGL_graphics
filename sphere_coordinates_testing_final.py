from importer import *








# x = sphere_vertexes()
# r = 0
# for i in range(len(x)):
#     print(x[i])
#     r +=1
# print(r)
def Normalize( pos):
    return np.array(getUnitVector(pos[0], pos[1], pos[2]))

def Translate(xyz):
    x,y,z = xyz
    return np.array([[x,0,0,0],
                      [0,y,0,0],
                      [0,0,z,0],
                      [0,0,0,1]],dtype = np.float32)


def lookat(eye,target,up):
    F = target[:3]-eye[:3]
    f = Normalize(F)
    U = Normalize(up[:3])
    s = np.cross(f, U)
    u = np.cross(s,f)
    M = np.array(np.identity(4))
    M[:3,:3] = np.vstack([s,u,-f])
    T = Translate(-eye)
    return multiply4by4_martix(M,T)

print(lookat(np.array([0,0,0]),np.array([0,0,3]),np.array([0,1,0])))
