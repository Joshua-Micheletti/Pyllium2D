from shared import *
from model.Mesh import Mesh, SquareMesh
from model.Shader import Shader
from model.Texture import Texture, TextureSheet
from model.Model import Model
from camera.Camera import Camera
from model.animation.Animation import Animation

import random

def load_scene():
    shaders["basic"] = Shader("../shader/basic/basic_vert.c", "../shader/basic/basic_frag.c")

    meshes["square"] = SquareMesh()
    meshes["base_mesh"] = SquareMesh()

    textures["test"] = Texture("../res/texture/background.png")

    textures["player"] = TextureSheet("../res/texture/gally.png", 10, 3)

    models["player"] = Animation("square", "player", "basic", "player", meshes["square"], textures["player"])
    models["player"].play_animation(8)
    models["player"].scale(models["player"].scale_x * 3, models["player"].scale_y * 3)

    models["floor"] = Model("base_mesh", "test", "basic", "floor", meshes["square"], textures["test"])
    models["floor"].scale(2000, 10)
    models["floor"].place(0, -100)

    for i in range(200):
        meshes["test_" + str(i)] = SquareMesh()
        models["test_" + str(i)] = Animation("test_" + str(i), "player", "basic", "", meshes["test_" + str(i)], textures["player"])
        models["test_" + str(i)].place(random.randint(-600, 600) , random.randint(-300, 300))
        models["test_" + str(i)].play_animation(8)

    physics_world = get_physics_world()

    physics_world.add_body("player", models["player"].x - models["player"].width / 2, models["player"].y - models["player"].height / 2, models["player"].width, models["player"].height, mass = 1, moving = True)
    physics_world.add_body("floor", models["floor"].x - models["floor"].width / 2, models["floor"].y - models["floor"].height / 2, models["floor"].width, models["floor"].height, 1, False)

    set_physics_world(physics_world)

    cameras["world"] = Camera()
