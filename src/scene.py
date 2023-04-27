from shared import models
from shared import batch
from shared import groups
from shared import physics_world
from shared import *
import pyglet
from mesh.Mesh import Mesh
from mesh.Sprite import Sprite
from mesh.TileMap import TileMap
from mesh.Tile import Tile
from mesh.dynamic.Player import Player
from structure.Structure import Structure

def load_scene():
    global models

    models["triangle"] = Mesh()

    models["triangle"].load_vertices(-0.5, -0.5, 0.0, 1.0, 0.0, 0.0
                                      0.5,  0.5, 0.0, 0.0, 1.0, 0.0,
                                      0.0,  0.5, 0.0, 0.0, 0.0, 1.0)


    # global models
    # global batch
    # global physics_world

    # world = []

    # tile_size = 64

    # for i in range(100):
    #     world.append([])
    #     for j in range(200):
    #         world[i].append(-1)

    # tilemap = TileMap()

    # tilemap.load_tilemap("../res/structure/Assets.png", 25, 25)


    # # models["car"] = Sprite("../res/texture/test.png")
    # # models["gally"] = Sprite("../res/texture/gally5.png")
    # # models["animation"] = Sprite("../res/animation/savannah-hodgins-idle.gif")
    # # models["background"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background1"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background2"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background3"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background4"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background5"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background6"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background7"] = Sprite("../res/texture/background.png", groups["background"])
    # models["background8"] = Sprite("../res/texture/background.png", groups["background"])

    # models["background1"].move(256, 0)
    # models["background2"].move(512, 0)
    # models["background3"].move(768, 0)
    # models["background4"].move(1024, 0)
    # models["background5"].move(1280, 0)
    # models["background6"].move(1536, 0)
    # models["background7"].move(1792, 0)
    # models["background8"].move(-20, 400)

    # # models["background"].scale(10)
    # models["player"] = Player("../res/texture/gally.png", groups["foreground"])
    # models["player"].load_sprite_sheet("../res/texture/gally.png", 10, 3, groups["foreground"])
    # models["player"].move(300, 300)
    # models["player"].scale(2)
    # # models["goldeen"] = Sprite("../res/animation/goldeen.gif")
    # # models["triangle"] = Model((-0.01, -0.01, 0.01, -0.01, 0.0, 0.01), (1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1))

    # physics_world = get_physics_world()

    # # physics_world.add_body("background", models["background"].x, models["background"].y, models["background"].width, models["background"].height, moving = False)
    # physics_world.add_body("background1", models["background1"].x, models["background1"].y, models["background1"].width, models["background1"].height, moving = False)
    # physics_world.add_body("background2", models["background2"].x, models["background2"].y, models["background2"].width, models["background2"].height, moving = False)
    # physics_world.add_body("background3", models["background3"].x, models["background3"].y, models["background3"].width, models["background3"].height, moving = False)
    # physics_world.add_body("background4", models["background4"].x, models["background4"].y, models["background4"].width, models["background4"].height, moving = False)
    # physics_world.add_body("background5", models["background5"].x, models["background5"].y, models["background5"].width, models["background5"].height, moving = False)
    # physics_world.add_body("background6", models["background6"].x, models["background6"].y, models["background6"].width, models["background6"].height, moving = False)
    # physics_world.add_body("background7", models["background7"].x, models["background7"].y, models["background7"].width, models["background7"].height, moving = False)
    # physics_world.add_body("background8", models["background8"].x, models["background8"].y, models["background8"].width, models["background8"].height, moving = False)
    # physics_world.add_body("player", models["player"].x, models["player"].y, models["player"].width, models["player"].height)

    # structure = Structure("../res/structure/tree.str")

    # map_str = Structure("../res/structure/map.str")

    # for i in range(len(map_str.cells)):
    #     for j in range(len(map_str.cells[i])):
    #         world[i][j] = map_str.cells[i][j]



    # # for i in range(len(structure.cells)):
    # #     for j in range(len(structure.cells[i])):
    # #         world[i][j] = structure.cells[i][j]

    # # for i in range(len(world)):
    # #     for j in range(len(world[i])):
    # #         if world[i][j] != -1:
    # #             models["world_tile_" + str(i) + "_" + str(j)] = Tile(tilemap.get_by_index(world[i][j]), groups["background"])
    # #             models["world_tile_" + str(i) + "_" + str(j)].move(j * tile_size, i * tile_size)
    # #             models["world_tile_" + str(i) + "_" + str(j)].scale(4)
    # #             physics_world.add_body("world_tile_" + str(i) + "_" + str(j), j * tile_size, i * tile_size, tile_size, tile_size, moving = False)


    # # models["test_tile"] = Tile(models["tilemap"].get_by_index(460), groups["background"])
    # # # models["test_tile"].move(0, 0)
    # # #
    # # models["test_tile_2"] = Tile(models["tilemap"].images[0][24], groups["background"])
    # # models["test_tile_2"].move(tile_size, tile_size)


    # set_physics_world(physics_world)


    # print("loaded the scene")
