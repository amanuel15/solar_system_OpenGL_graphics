text_circle = open("text_files/circle_coordinates.txt", "r")
text_triangles = open("text_files/triangle_coordinates.txt", "w")
text_triangles1 = open("text_files/triangle_coordinates.txt", "r")


def create_coordinates(file_a, file_b):
    for i in range(len(file_a)-1):
        text_triangles.write(file_a[i])
        text_triangles.write(",")
        text_triangles.write(str(file_b))
        text_triangles.write(",")
        text_triangles.write(file_a[i+1])
        text_triangles.write(",")
        text_triangles.write("\n")


def file_parser(line):
    c_b, o_b = 0, 0
    final_coordinates = []
    bracket_count = lines.count("]")
    for i in range(bracket_count):
        if c_b == 0:
            o_b, c_b = lines.index("["), lines.index("]")
        else:
            o_b, c_b = lines[c_b + 1:].index("[") + c_b + 1, lines[c_b + 1:].index("]") + c_b + 1
        coordinates = line[o_b:c_b+1]
        final_coordinates.append(coordinates)
    return final_coordinates


middle_of_circle = [0, 0, 0, 1, 1, 1,  0.5, 0.5]
x = 0
for lines in text_circle:
    x = file_parser(lines)

create_coordinates(x, middle_of_circle)
# for lines in text_triangles1:
#     print(lines)
