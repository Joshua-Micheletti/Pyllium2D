from termcolor import colored
from model.Mesh import Mesh, SquareMesh
from model.Shader import Shader
from model.Texture import Texture, TextureSheet
from model.Model import Model
from model.animation.Animation import Animation

class ResourceManager:

    def __init__(self):
        self.models = dict()
        self.meshes = dict()
        self.textures = dict()
        self.shaders = dict()

        self.rendering_buffer = dict()


    def add_mesh(self, name = "", type = "square"):
        if len(name) == 0 or not isinstance(name, str):
            name = "mesh_" + str(len(self.meshes) + 1)
            print(f"invalid mesh name, new mesh name: {name}")

        if name in self.meshes:
            print(colored("mesh name already exists", "red"))
            return(False)

        if type == "square":
            self.meshes[name] = SquareMesh()
        else:
            self.meshes[name] = Mesh()

        return(self.meshes[name])


    def add_texture(self, name = "", path = ""):
        if len(name) == 0 or not isinstance(name, str):
            name = "texture_" + str(len(self.textures) + 1)
            print(f"invalid texture name, new texture name: {name}")

        if name in self.textures:
            print(colored("texture name already exists", "red"))
            return(False)

        self.textures[name] = Texture(path)

        return(self.textures[name])


    def add_texturesheet(self, name = "", path = "", rows = 0, columns = 0):
        if len(name) == 0 or not isinstance(name, str):
            name = "texturesheet_" + str(len(self.meshes) + 1)
            print(f"invalid texturesheet name, new texturesheet name: {name}")

        if name in self.textures:
            print(colored("texture name already exists", "red"))
            return(False)

        self.textures[name] = TextureSheet(path, rows, columns)

        return(self.textures[name])


    def add_shader(self, name = "", vertex_path = "", fragment_path = ""):
        if len(name) == 0 or not isinstance(name, str):
            name = "shader_" + str(len(self.shaders) + 1)
            print(f"invalid shader name, new shader name: {name}")

        if name in self.shaders:
            print(colored("shader name already exists", "red"))
            return(False)

        self.shaders[name] = Shader(vertex_path, fragment_path)

        return(self.shaders[name])


    def add_model(self, name = "", type = "static", mesh = "", texture = "", shader = "", rendering_order = 0):
        if len(name) == 0 or not isinstance(name, str):
            name = "model_" + str(len(self.models) + 1)
            print(f"invalid model name, new model name: {name}")

        if name in self.models:
            print(colored("model name already exists", "red"))
            return(False)

        if len(mesh) == 0 or not isinstance(mesh, str) or not mesh in self.meshes:
            print(colored("invalid mesh name", "red"))
            return(False)

        if len(texture) == 0 or not isinstance(texture, str) or not texture in self.textures:
            print(colored("invalid texture name", "red"))
            return(False)

        if len(shader) == 0 or not isinstance(shader, str) or not shader in self.shaders:
            print(colored("invalid shader name", "red"))
            return(False)

        if type == "static":
            self.models[name] = Model(mesh, texture, shader, self.meshes[mesh], self.textures[texture], rendering_order)
        elif type == "animation":
            self.models[name] = Animation(mesh, texture, shader, self.meshes[mesh], self.textures[texture], rendering_order)

        if not str(rendering_order) in self.rendering_buffer:
            self.rendering_buffer[str(rendering_order)] = dict()
            self.rendering_buffer[str(rendering_order)][shader] = []
            self.rendering_buffer[str(rendering_order)][shader].append(self.models[name])

        else:
            if not shader in self.rendering_buffer[str(rendering_order)]:
                self.rendering_buffer[str(rendering_order)][shader] = []
                self.rendering_buffer[str(rendering_order)][shader].append(self.models[name])
            else:
                self.rendering_buffer[str(rendering_order)][shader].append(self.models[name])

        self.rendering_buffer = dict(sorted(self.rendering_buffer.items()))

        return(self.models[name])
