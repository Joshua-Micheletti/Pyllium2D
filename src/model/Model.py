from pyrr import Matrix44
import numpy as np
import pyrr

class Model:
    def __init__(self, mesh = "", texture = "", shader = "", mesh_obj = None, texture_obj = None, rendering_order = 0):
        self.mesh = mesh
        self.texture = texture
        self.shader = shader

        self.x = 0
        self.y = 0
        self.width = 1
        self.height = 1
        self.scale_x = 64
        self.scale_y = 64
        self.mesh_width = 0
        self.mesh_height = 0
        self.texture_width = 0
        self.texture_height = 0
        self.model_matrix = Matrix44.identity()
        self.translation_matrix = Matrix44.identity()
        self.scale_matrix = Matrix44.identity()

        self.rendering_order = rendering_order

        if mesh_obj is not None:
            self.set_mesh(mesh, mesh_obj)
        if texture_obj is not None:
            self.set_texture(texture, texture_obj)

    def calculate_model_matrix(self):
        self.model_matrix = Matrix44.identity()
        self.translation_matrix = Matrix44.from_translation(np.array([self.x, self.y, 1]))
        self.scale_matrix = Matrix44.from_scale(np.array([self.scale_x, self.scale_y, 1]))
        self.model_matrix = self.model_matrix * self.translation_matrix * self.scale_matrix

    def set_mesh(self, mesh, mesh_obj):
        self.mesh = mesh
        self.mesh_width = mesh_obj.width
        self.mesh_height = mesh_obj.height
        self.width = self.mesh_width * self.scale_x
        self.height = self.mesh_height * self.scale_y

    def set_texture(self, texture, texture_obj):
        self.texture = texture
        self.texture_width = texture_obj.get_size()[0]
        self.texture_height = texture_obj.get_size()[1]

        self.scale(self.texture_width, self.texture_height)

    def move(self, x, y):
        if x == 0 and y == 0:
            return

        self.x += x
        self.y += y
        self.calculate_model_matrix()

        return(self)

    def scale(self, x, y):
        if x == self.scale_x and y == self.scale_y:
            return

        self.scale_x = x
        self.scale_y = y

        self.width = self.mesh_width * self.scale_x
        self.height = self.mesh_height * self.scale_y

        self.calculate_model_matrix()

        return(self)

    def scale_by(self, x, y):
        if x == 1 and y == 1:
            return

        self.scale(self.scale_x * x, self.scale_y * y)

        return(self)



    def place(self, x, y):
        if x == self.x and y == self.y:
            return

        self.x = x
        self.y = y
        self.calculate_model_matrix()

        return(self)
