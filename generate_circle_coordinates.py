from math import *

#nigga damn, all dis shit do is rotate dem hoes

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

texture_coordinates = generate_Circle([0.5, 0], 1)
for i in range(len(texture_coordinates)):
    texture_coordinates[i] = [texture_coordinates[i][0]+0.5, texture_coordinates[i][1]+0.5]

x = generate_Circle([0.2, 0, 0], 1)
# text = open("text_files/circle_coordinates.txt", "w")

for i in range(len(x)):
    final = [x[i][0], x[i][1], x[i][2],   1, 1, 1,   texture_coordinates[i][0], texture_coordinates[i][1]]
    print(final)
# text.write(str(final))
# text.write("\n")
