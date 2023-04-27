from OpenGL.GL.shaders import compileProgram, compileShader

class Shader:
    def __init__():
        print("new shader")
        self.program = None
        self.vertex_path = None
        self.fragment_path = None
        self.vertex_src = None
        self.fragment_src = None

    def compile_program(self, vertex_path, fragment_path):
        self.vertex_path = vertex_path
        self.fragment_path = fragment_path

        with open(vertex_path, 'r') as f:
            self.vertex_src = f.readlines()
        with open(fragment_path, 'r') as f:
            self.fragmant_src = f.readlines()

        self.program = compileProgram(
            compileShader
        )
