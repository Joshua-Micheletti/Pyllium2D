# from shared import models
# from shared import batch
# from shared import groups
# from shared import physics_world
# from shared import *
# import pyglet
# from mesh.Mesh import Mesh
# from mesh.Sprite import Sprite
# from mesh.TileMap import TileMap
# from mesh.Tile import Tile
# from shader.Shader import Shader
# from mesh.dynamic.Player import Player
# from structure.Structure import Structure
from shared import *
from model.Mesh import Mesh
from model.Shader import Shader
from model.Texture import Texture
from model.Model import Model
from camera.Camera import Camera

def load_scene():
    global models

    shaders["basic"] = Shader()
    shaders["basic"].compile_program("../shader/basic/basic_vert.c", "../shader/basic/basic_frag.c")

    meshes["square"] = Mesh()
    meshes["square"].load_vertices([-0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                     0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
                                     0.5,  0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0,
                                    -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                    -0.5,  0.5, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0,
                                     0.5,  0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0])
    meshes["rectangle"] = Mesh()
    meshes["rectangle"].load_vertices([-0.2, -0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                        0.2, -0.6, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
                                        0.2,  0.6, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0,
                                       -0.2, -0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                       -0.2,  0.6, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0,
                                        0.2,  0.6, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0])

    textures["test"] = Texture()
    textures["test"].load_image("../res/texture/background.png")

    models["player"] = Model("square", "test", "basic", "player", meshes["square"], textures["test"])
    models["player"].place(0, 200)

    models["floor"] = Model("square", "test", "basic", "floor", meshes["square"], textures["test"])

    for i in range(0):
        models["test_" + str(i)] = Model("square", "test", "basic", "", meshes["square"], textures["test"])

    models["floor"].scale(2000, 10)
    models["floor"].place(0, -100)

    physics_world = get_physics_world()

    physics_world.add_body("player", models["player"].x - models["player"].width / 2, models["player"].y - models["player"].height / 2, models["player"].width, models["player"].height, mass = 1, moving = True)
    physics_world.add_body("floor", models["floor"].x - models["floor"].width / 2, models["floor"].y - models["floor"].height / 2, models["floor"].width, models["floor"].height, 1, False)

    set_physics_world(physics_world)

    cameras["world"] = Camera()
