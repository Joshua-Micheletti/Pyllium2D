class Model:

    def __init__(self):
        self.mesh = None
        self.texture = None
        self.shader = None

    def set_mesh(self, mesh):
        self.mesh = mesh
    
    def set_texture(self, texture):
        self.texture = texture

    def set_shader(self, shader):
        self.shader = shader