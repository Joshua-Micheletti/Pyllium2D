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
from model.Tilemap import Tilemap

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
    world = Tilemap(25, 25, "tilemap", 64)

    world.add_structure(structure.cells, 0, 0)

    world.create_tiles()

    set_world(world)
    set_resource_manager(rm)
