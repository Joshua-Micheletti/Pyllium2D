from shared import *
from model.Mesh import Mesh, SquareMesh
from model.Shader import Shader
from model.Texture import Texture, TextureSheet
from model.Model import Model
from entity.Entity import Entity, Player
from camera.Camera import Camera, FollowCamera
from model.animation.Animation import Animation
from structure.Structure import Structure
from renderer.ResourceManager import ResourceManager

import random

def load_scene():
    rm = get_resource_manager()

    rm.add_shader("basic", "../shader/basic/basic_vert.c", "../shader/basic/basic_frag.c")

    rm.add_mesh("square", "square")
    rm.add_mesh("base_mesh", "square")
    rm.add_mesh("tile_mesh", "square")

    rm.add_texture("test", "../res/texture/background.png")
    rm.add_texturesheet("player", "../res/texture/gally.png", 10, 3)
    rm.add_texturesheet("tilemap", "../res/structure/Assets.png", 25, 25)

    rm.add_model(name="player", type="animation", mesh="square", texture="player", shader="basic", rendering_order=2).scale_by(3, 3)
    rm.add_model("floor", "static", "base_mesh", "test", "basic", 0).scale(2000, 10).place(0, -100)

    physics_world = get_physics_world()

    physics_world.add_body("player", rm.models["player"].x - rm.models["player"].width / 2, rm.models["player"].y - rm.models["player"].height / 2, rm.models["player"].width, rm.models["player"].height, mass = 1, moving = True)
    physics_world.add_body("floor", rm.models["floor"].x - rm.models["floor"].width / 2, rm.models["floor"].y - rm.models["floor"].height / 2, rm.models["floor"].width, rm.models["floor"].height, 1, False)

    set_physics_world(physics_world)

    entities["player"] = Player("player", "player")
    entities["floor"] = Entity("floor", "floor")

    cameras["world"] = FollowCamera("player")

    structure = Structure("../res/structure/tree.str")

    world = get_world()
    world = []

    tile_size = 64

    for i in range(25):
        world.append([])
        for j in range(25):
            world[i].append(j * 25 + i)
            uvs = rm.textures["tilemap"].get_uv(j, i)
            if uvs != False:
                rm.add_mesh("tile_mesh_" + str(i) + "_" + str(j), "square").set_uv(uvs[0], uvs[1], rm.textures["tilemap"].tile_uv_width, rm.textures["tilemap"].tile_uv_height)
                rm.add_model("tile_" + str(i) + "_" + str(j), "static", "tile_mesh_" + str(i) + "_" + str(j), "tilemap", "basic", 1).place(i * tile_size, j * tile_size).scale_by(4, 4)

    set_world(world)
    set_resource_manager(rm)
