from termcolor import colored

import numpy as np
from OpenGL.GL import *

# Class for handling classic OpenGL meshes (vertices, shader)
class Mesh():
    """Class for handling classic OpenGL models (vertices, shader)"""

    def __init__(self):
        self.vertices = None
        self.vertex_count = None
        self.vao = None
        self.vbo = None
        self.width = 0
        self.height = 0

    def load_vertices(self, vertices):
        numbers_per_vertex = 8

        min_x = 2
        max_x = -2
        min_y = 2
        max_y = -2

        for i in range(int(len(vertices) / numbers_per_vertex)):
            if vertices[i*numbers_per_vertex] > max_x:
                max_x = vertices[i*numbers_per_vertex]
            if vertices[i*numbers_per_vertex] < min_x:
                min_x = vertices[i*numbers_per_vertex]
            if vertices[i*numbers_per_vertex + 1] > max_y:
                max_y = vertices[i*numbers_per_vertex + 1]
            if vertices[i*numbers_per_vertex + 1] < min_y:
                min_y = vertices[i*numbers_per_vertex + 1]

        self.width = max_x - min_x
        self.height = max_y - min_y

        self.vertices = np.array(vertices, dtype=np.float32)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        self.vertex_count = int(len(vertices) / 8)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))

    # constructor method to fully setup the object
    # def __init__(self, vertex, colors, vertex_shader_source = "../shader/basic/basic_vert.c", fragment_shader_source = "../shader/basic/basic_frag.c"):
    #     self.vertex_shader = None
    #     self.fragment_shader = None
    #     self.shader_program = None
    #     self.vertices = None

    #     self.create_shader(vertex_shader_source, fragment_shader_source)
    #     self.set_vertices(vertex, colors)

    # # method for setting the vertex shader from a file path
    # def set_vertex_shader(self, vertex_shader_source):
    #     try:
    #         vert = open(vertex_shader_source)
    #         self.vertex_shader = Shader(vert.read(), 'vertex')
    #         vert.close()
    #         return(1)

    #     except Exception as e:
    #         print(colored("Vertex file open error", "red"))
    #         print(colored(e, "red"))
    #         return(0)

    # # method for setting the fragment shader from a file path
    # def set_fragment_shader(self, fragment_shader_source):
    #     try:
    #         frag = open(fragment_shader_source)
    #         self.fragment_shader = Shader(frag.read(), 'fragment')
    #         frag.close()
    #         return(1)

    #     except Exception as e:
    #         print(colored("Fragment file open error", "red"))
    #         print(colored(e, "red"))
    #         return(0)

    # # method for creating the shader object from the vertex and fragment shader
    # def create_shader(self, vertex_shader_source = "../shader/basic/basic_vert.c", fragment_shader_source = "../shader/basic/basic_frag.c"):
    #     if not self.set_vertex_shader(vertex_shader_source):
    #         return(0)

    #     if  not self.set_fragment_shader(fragment_shader_source):
    #         return(0)

    #     self.shader_program = ShaderProgram(self.vertex_shader, self.fragment_shader)

    # # method for passing the vertices to the shader object
    # def set_vertices(self, vertex, colors):
    #     if self.shader_program == None:
    #         print(colored("Shader program not initialized", "red"))
    #         return(0)

    #     if len(vertex) % 2 != 0:
    #         print(colored("Vertices count isn't a multiple of 2", "red"))
    #         return(0)

    #     if len(colors) % 4 != 0:
    #         print(colored("Colors count isn't a multiple of 4", "red"))
    #         return(0)

    #     if len(vertex) / 2 != len(colors) / 4:
    #         print(colored("Vertices - Colors mismatch", "red"))
    #         return(0)

    #     self.vertices = self.shader_program.vertex_list(int(len(vertex) / 2), GL_TRIANGLES, batch = batch)
    #     self.vertices.position = vertex
    #     self.vertices.colors = colors


    # def create_model(self, vertex, colors, vertex_shader_source = "../shader/basic/basic_vert.c", fragment_shader_source = "../shader/basic/basic_frag.c"):
    #     self.create_shader(vertex_shader_source, fragment_shader_source)
    #     self.set_vertices(vertex, colors)
