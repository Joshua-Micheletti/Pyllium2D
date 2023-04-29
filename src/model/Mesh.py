from termcolor import colored

import numpy as np
from OpenGL.GL import *

# Class for handling classic OpenGL meshes (vertices, shader)
class Mesh():
    """Class for handling classic OpenGL models (vertices, shader)"""

    def __init__(self):
        self.formatted_vertices = None
        self.vertices = None
        self.vertex_count = None
        self.vao = None
        self.vbo = None
        self.width = 0
        self.height = 0

    def load_vertices(self, vertices):
        self.vertices = vertices

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

        self.vertex_count = int(len(self.vertices) / 8)

        self.generate_ogl_buffers()


    def generate_ogl_buffers(self):
        self.destroy()

        self.formatted_vertices = np.array(self.vertices, dtype=np.float32)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.formatted_vertices.nbytes, self.formatted_vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))

    def destroy(self):
        if self.vao is not None:
            glDeleteVertexArrays(1, (self.vao,))
        if self.vbo is not None:
            glDeleteBuffers(1, (self.vbo,))

    
class SquareMesh(Mesh):

    def __init__(self):
        super().__init__()

        self.load_vertices([-0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                             0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
                             0.5,  0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0,
                            -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                            -0.5,  0.5, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0,
                             0.5,  0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0])
        
    def set_uv(self, x, y, w, h):
        self.load_vertices([-0.5, -0.5, 0.0, 0.0, 0.0, 0.0, x  , y,
                             0.5, -0.5, 0.0, 1.0, 0.0, 0.0, x+w, y,
                             0.5,  0.5, 0.0, 1.0, 1.0, 0.0, x+w, y+h,
                            -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, x  , y,
                            -0.5,  0.5, 0.0, 0.0, 1.0, 0.0, x  , y+h,
                             0.5,  0.5, 0.0, 1.0, 1.0, 0.0, x+w, y+h])
        
