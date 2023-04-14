from shared import batch
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.gl import *
from termcolor import colored

# Class for handling classic OpenGL models (vertices, shader)
class Model():
    """Class for handling classing OpenGL models (vertices, shader).\n
    Model()\n
    Model(vertex, colors, vertex_shader_source = "../shader/basic/basic_vert.c", fragment_shader_source = "../shader/basic/basic_frag.c")"""

    # default constructor method
    def __init__(self):
        self.vertex_shader = None
        self.fragment_shader = None
        self.shader_program = None
        self.vertices = None

    # constructor method to fully setup the object
    def __init__(self, vertex, colors, vertex_shader_source = "../shader/basic/basic_vert.c", fragment_shader_source = "../shader/basic/basic_frag.c"):
        self.vertex_shader = None
        self.fragment_shader = None
        self.shader_program = None
        self.vertices = None

        self.create_shader(vertex_shader_source, fragment_shader_source)
        self.set_vertices(vertex, colors)

    # method for setting the vertex shader from a file path
    def set_vertex_shader(self, vertex_shader_source):
        try:
            vert = open(vertex_shader_source)
            self.vertex_shader = Shader(vert.read(), 'vertex')
            vert.close()
            return(1)

        except Exception as e:
            print(colored("Vertex file open error", "red"))
            print(colored(e, "red"))
            return(0)

    # method for setting the fragment shader from a file path
    def set_fragment_shader(self, fragment_shader_source):
        try:
            frag = open(fragment_shader_source)
            self.fragment_shader = Shader(frag.read(), 'fragment')
            frag.close()
            return(1)

        except Exception as e:
            print(colored("Fragment file open error", "red"))
            print(colored(e, "red"))
            return(0)

    # method for creating the shader object from the vertex and fragment shader
    def create_shader(self, vertex_shader_source = "../shader/basic/basic_vert.c", fragment_shader_source = "../shader/basic/basic_frag.c"):
        if not self.set_vertex_shader(vertex_shader_source):
            return(0)

        if  not self.set_fragment_shader(fragment_shader_source):
            return(0)

        self.shader_program = ShaderProgram(self.vertex_shader, self.fragment_shader)

    # method for passing the vertices to the shader object
    def set_vertices(self, vertex, colors):
        if self.shader_program == None:
            print(colored("Shader program not initialized", "red"))
            return(0)

        if len(vertex) % 2 != 0:
            print(colored("Vertices count isn't a multiple of 2", "red"))
            return(0)

        if len(colors) % 4 != 0:
            print(colored("Colors count isn't a multiple of 4", "red"))
            return(0)

        if len(vertex) / 2 != len(colors) / 4:
            print(colored("Vertices - Colors mismatch", "red"))
            return(0)

        self.vertices = self.shader_program.vertex_list(int(len(vertex) / 2), GL_TRIANGLES, batch = batch)
        self.vertices.position = vertex
        self.vertices.colors = colors


    # def create_model(self, vertex, colors, vertex_shader_source = "../shader/basic/basic_vert.c", fragment_shader_source = "../shader/basic/basic_frag.c"):
    #     self.create_shader(vertex_shader_source, fragment_shader_source)
    #     self.set_vertices(vertex, colors)
