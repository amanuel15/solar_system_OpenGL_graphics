from importer import *


class Shader:
    def __init__(self):
        self.delay = 17
        self.translational_increment = 1
        self.display = (1366, 768)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL | FULLSCREEN)
        glClearColor(.30, 0.20, 0.20, 1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        pygame.init()
        self.lighting = [0, 0, 0]
        self.newMix = [0, 0, 0]
        self.sunPos, self.mercuryPos, self.venusPos, self.earthPos, self.marsPos, self.jupiterPos, self.saturnPos, self.uranusPos, self.neptunePos, self.plutoPos = [0, 0, -1], [-5, 0, -1], [-7, 0, -1], [-8, 0, -1], [-10, 0, -1], [-16, 0, -1], [-21, 0, -1], [-24, 0, -1], [-27, 0, -1], [-31, 0, -1]
        self.sunRot, self.mercuryRot, self.venusRot, self.earthRot, self.marsRot, self.jupiterRot, self.saturnRot, self.uranusRot, self.neptuneRot, self.plutoRot = [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]
        self.sunScale, self.mercuryScale, self.venusScale, self.earthScale, self.marsScale, self.jupiterScale, self.saturnScale, self.uranusScale, self.neptuneScale, self.plutoScale = 13*np.array([1, 1, 1], dtype=np.float32), .5*np.array([1, 1, 1], dtype=np.float32), .8*np.array([1, 1, 1], dtype=np.float32), np.array([1, 1, 1], dtype=np.float32), 1.5*np.array([1, 1, 1], dtype=np.float32), 7*np.array([1, 1, 1], dtype=np.float32), 6*np.array([1, 1, 1], dtype=np.float32), 4*np.array([1, 1, 1], dtype=np.float32), 3*np.array([1, 1, 1], dtype=np.float32), .3*np.array([1, 1, 1], dtype=np.float32)
        self.allPositions = [self.sunPos, self.mercuryPos, self.venusPos, self.earthPos, self.marsPos, self.jupiterPos, self.saturnPos, self.uranusPos, self.neptunePos, self.plutoPos]
        self.allRotations = [self.sunRot, self.mercuryRot, self.venusRot, self.earthRot, self.marsRot, self.jupiterRot, self.saturnRot, self.uranusRot, self.neptuneRot, self.plutoRot]
        self.allScale = [self.sunScale, self.mercuryScale, self.venusScale, self.earthScale, self.marsScale, self.jupiterScale, self.saturnScale, self.uranusScale, self.neptuneScale, self.plutoScale]
        self.celestialPos = [0, 27, -48]
        self.celestialRot = [-0.5600000000000003, 0, 0]
        self.Shader_List = []
        self.Rotational_Degrees = [1, .8, -3, 2, .2, -4, 2, 1.4, 7, -4]
        self.init()

    def init(self):
        x = load_sphere2()
        y = load_skymap()
        list_images = ["shaders6/images/a.jpeg", "shaders6/images/f.jpeg", "shaders6/images/b.jpg", "shaders6/images/c.jpg", "shaders6/images/d.jpeg", "shaders6/images/g.jpeg", "shaders6/images/e.jpeg", "shaders6/images/i.jpg", "shaders6/images/c.jpg", "shaders6/images/f.jpeg"]
        for i in range(10):
            self.Shader_List.append([Shaderprogram(x, list_images[i], "shaders6/tex.png"), int(len(x)/4), self.allPositions[i], self.allRotations[i], self.allScale[i]])
        self.Shader_List.append([Shaderprogram(y, "shaders6/images/skymap.jpg", "shaders6/images/skymap2.jpg"), 24, [0, 0, 10], [0, 0, 0], [10, 10, 10]])
    
    @staticmethod
    def getfilecontents(filename):
        p = os.path.join(os.getcwd(), "shaders8", filename)
        return open(p, 'r').read()

    def draw_all(self):
        self.allPositions = [self.sunPos, self.mercuryPos, self.venusPos, self.earthPos, self.marsPos, self.jupiterPos, self.saturnPos, self.uranusPos, self.neptunePos, self.plutoPos]
        for i in range(len(self.allPositions)):
            self.Shader_List[i][2] = self.allPositions[i]
            self.Shader_List[i][3] = self.allRotations[i]
        for i in self.Shader_List:
            self.draw(i[0], i[1], i[2], i[3], i[4])

    def draw(self, shader_file, number_of_quads, positions, rotations, scales):
        perspective = [45.0, (self.display[0]/self.display[1]), .1, 200.0]
        program = shader_file.programs()
        glUseProgram(program)
        glBindVertexArray(shader_file.triangleVAO)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, shader_file.texture)
        shader_file.translate(positions)
        shader_file.celestial_translate(self.celestialPos)
        shader_file.celestial_rotate(self.celestialRot)
        shader_file.rotate(rotations)
        shader_file.apply_textures(self.newMix)
        shader_file.scale(scales)
        shader_file.lighting(self.lighting)
        shader_file.projections(perspective)
        glDrawArrays(GL_QUADS, 0, number_of_quads*4)

    def revolve_planets(self):
        self.mercuryPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[1]), self.mercuryPos, [0, 0, 0])
        self.venusPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[2]), self.venusPos, [0, 0, 0])
        self.earthPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[3]), self.earthPos, [0, 0, 0])
        self.marsPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[4]), self.marsPos, [0, 0, 0])
        self.jupiterPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[5]), self.jupiterPos, [0, 0, 0])
        self.saturnPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[6]), self.saturnPos, [0, 0, 0])
        self.uranusPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[7]), self.uranusPos, [0, 0, 0])
        self.neptunePos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[8]), self.neptunePos, [0, 0, 0])
        self.plutoPos = multiply3by1_matrix(rotateY(self.Rotational_Degrees[9]), self.plutoPos, [0, 0, 0])

    def rotate_bodies(self):
        self.sunRot[1] += 1
        self.mercuryRot[1] += 1
        self.venusRot[1] += 1
        self.earthRot[1] += 1
        self.marsRot[1] += 1
        self.jupiterRot[1] += 1
        self.saturnRot[1] += 1
        self.uranusRot[1] += 1
        self.neptuneRot[1] += 1
        self.plutoRot[1] += 1

    def main(self):
        rotate = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                if self.celestialPos[2] <= 25:
                    self.celestialPos[2] += self.translational_increment
            if key[pygame.K_s]:
                if self.celestialPos[2] >= -55:
                    self.celestialPos[2] -= self.translational_increment
            if key[pygame.K_d]:
                if self.celestialPos[0] >= -35:
                    self.celestialPos[0] -= self.translational_increment
            if key[pygame.K_a]:
                if self.celestialPos[0] <= 25:
                    self.celestialPos[0] += self.translational_increment
            if key[pygame.K_KP8]:
                if self.celestialPos[1] >= -40:
                    self.celestialPos[1] -= self.translational_increment
            if key[pygame.K_KP2]:
                if self.celestialPos[1] <= 40:
                    self.celestialPos[1] += self.translational_increment
            if key[pygame.K_UP]:
                self.celestialRot[0] -= .01
            if key[pygame.K_DOWN]:
                self.celestialRot[0] += .01
            if key[pygame.K_LEFT]:
                self.celestialRot[1] -= .01
            if key[pygame.K_RIGHT]:
                self.celestialRot[1] += .01
            if key[pygame.K_q]:
                self.newMix[0] += .005
            if key[pygame.K_e]:
                self.newMix[0] -= .005
            if key[pygame.K_l]:
                self.lighting[0] += 0.01
                self.lighting[1] += 0.01
                self.lighting[2] += 0.01
            if key[pygame.K_k]:
                self.lighting[0] -= 0.01
                self.lighting[1] -= 0.01
                self.lighting[2] -= 0.01
            if key[pygame.K_x]:
                pygame.mixer.music.load("shaders6/X.mp3")
                pygame.mixer.music.play(0, 0.0)
            if key[pygame.K_RETURN]:
                rotate = False
            if key[pygame.K_SPACE]:
                rotate = True
            if key[pygame.K_p]:
                self.delay += 5
            if key[pygame.K_o]:
                self.delay -= 5
            if key[pygame.K_m]:
                self.translational_increment += .1
            if key[pygame.K_n]:
                self.translational_increment -= .1
            if key[pygame.K_ESCAPE]:
                pygame.quit()
                quit()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw_all()
            if rotate:
                self.revolve_planets()
                self.rotate_bodies()
            pygame.display.flip()
            pygame.time.wait(self.delay)


class Shaderprogram:
    def __init__(self, vertex, image, image1):
        self.triangleVAO = 0
        self.texture = 0
        self.vertex = vertex
        self.images1 = self.image_data(image)
        self.images2 = self.image_data(image1)
        self.program = glCreateProgram()
        vertexshadercontent = self.getfilecontents("triangle.vertex2.shader")
        fragmentshadercontent = self.getfilecontents("triangle.fragment.shader")
        vertexshader = compileShader(vertexshadercontent, GL_VERTEX_SHADER)
        fragmentshader = compileShader(fragmentshadercontent, GL_FRAGMENT_SHADER)
        glAttachShader(self.program, vertexshader)
        glAttachShader(self.program, fragmentshader)
        glLinkProgram(self.program)
        self.init()

    def init(self):
        c = Shaders(self.vertex)
        self.add_shape(c, self.images1, self.images2)

    def add_shape(self, shader, images, images1):
        self.draw(shader.tvaos(), shader.tvbos(), shader.vertex(), shader.textures(), shader.textures2(), images,
                  images1)

    def draw(self, tvao, tvbo, vertex, texture, texture1, images, images1):
        glBindBuffer(GL_ARRAY_BUFFER, tvbo)
        glBufferData(GL_ARRAY_BUFFER, vertex.nbytes, vertex, GL_STATIC_DRAW)
        glBindVertexArray(tvao)
        self.triangleVAO = tvao
        positionlocation = glGetAttribLocation(self.program, "position")
        glVertexAttribPointer(positionlocation, 3, GL_FLOAT, GL_FALSE,
                              8 * vertex.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(positionlocation)
        colorlocation = glGetAttribLocation(self.program, "color")
        glVertexAttribPointer(colorlocation, 3, GL_FLOAT, GL_FALSE,
                              8 * vertex.itemsize, ctypes.c_void_p(12))
        glEnableVertexAttribArray(colorlocation)
        textlocation = glGetAttribLocation(self.program, "texCoord")
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE,
                              8 * vertex.itemsize, ctypes.c_void_p(24))
        glEnableVertexAttribArray(textlocation)

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, images[0], images[1], 0, GL_RGB, GL_UNSIGNED_BYTE, images[2])

        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, texture1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, images1[0], images1[1], 0, GL_RGB, GL_UNSIGNED_BYTE, images1[2])
        self.texture = texture

    def scale(self, size):
        scalesize = glGetUniformLocation(self.program, "scale")
        glUniform3fv(scalesize, 1,  size)

    def projections(self, newprojloc):
        projloc = glGetUniformLocation(self.program, "projection")
        glUniform4fv(projloc, 1, newprojloc)

    def lighting(self, light):
        fakelighting = glGetUniformLocation(self.program, "fakeLighting")
        glUniform3fv(fakelighting, 1, light)

    def apply_textures(self, newmix):
        uniloc1 = glGetUniformLocation(self.program, "texSampler")
        glUniform1i(uniloc1, 0)
        uniloc2 = glGetUniformLocation(self.program, "texSampler2")
        glUniform1i(uniloc2, 1)
        mix = glGetUniformLocation(self.program, "mixe")
        glUniform3fv(mix, 1, newmix)

    def celestial_translate(self, pos):
        celestialpos = glGetUniformLocation(self.program, "celestialPos")
        glUniform3fv(celestialpos, 1, pos)

    def celestial_rotate(self, rot):
        celestialrot = glGetUniformLocation(self.program, "celestialRot")
        glUniform3fv(celestialrot, 1, rot)

    def translate(self, pos):
        posloc = glGetUniformLocation(self.program, "newPos")
        glUniform3fv(posloc, 1, pos)

    def rotate(self, rot):
        rotloc = glGetUniformLocation(self.program, "newVec")
        glUniform3fv(rotloc, 1, rot)

    def programs(self):
        return self.program

    @staticmethod
    def image_data(directory):
        image = Image.open(directory)
        width, height = image.size
        image_data = np.array(list(image.getdata()), dtype=np.uint8)
        return width, height, image_data

    @staticmethod
    def getfilecontents(filename):
        p = os.path.join(os.getcwd(), "shaders8", filename)
        return open(p, 'r').read()


class Shaders:
    def __init__(self, vertexes):
        self.vertexes1 = np.array(vertexes, np.float32)
        self.tVBO = glGenBuffers(1)
        self.tVAO = glGenVertexArrays(1)
        self.texture = glGenTextures(1)
        self.texture1 = glGenTextures(1)

    def tvaos(self):
        return self.tVAO

    def tvbos(self):
        return self.tVBO

    def textures(self):
        return self.texture

    def textures2(self):
        return self.texture1

    def vertex(self):
        return self.vertexes1


test = Shader()
test.main()
