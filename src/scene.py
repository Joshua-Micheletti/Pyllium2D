from shared import models
from shared import batch
from shared import groups
from shared import physics_bodies
import pyglet
from model.Model import Model
from model.Sprite import Sprite
from physics.PhysicsBody import PhysicsBody

def load_scene():
    global models
    global batch

    # models["car"] = Sprite("../res/texture/test.png")
    # models["gally"] = Sprite("../res/texture/gally5.png")
    # models["animation"] = Sprite("../res/animation/savannah-hodgins-idle.gif")
    models["background"] = Sprite("../res/texture/background.png", groups["background"])
    models["background1"] = Sprite("../res/texture/background.png", groups["background"])
    models["background2"] = Sprite("../res/texture/background.png", groups["background"])
    models["background3"] = Sprite("../res/texture/background.png", groups["background"])
    models["background4"] = Sprite("../res/texture/background.png", groups["background"])
    models["background5"] = Sprite("../res/texture/background.png", groups["background"])
    models["background6"] = Sprite("../res/texture/background.png", groups["background"])
    models["background7"] = Sprite("../res/texture/background.png", groups["background"])
    models["background8"] = Sprite("../res/texture/background.png", groups["background"])

    models["background1"].move(256, 0)
    models["background2"].move(512, 0)
    models["background3"].move(768, 0)
    models["background4"].move(1024, 0)
    models["background5"].move(1280, 0)
    models["background6"].move(1536, 0)
    models["background7"].move(1792, 0)
    models["background8"].move(-20, 400)

    # models["background"].scale(10)
    models["player"] = Sprite("../res/animation/growlithe.gif", groups["foreground"])
    models["player"].move(300, 300)
    # models["goldeen"] = Sprite("../res/animation/goldeen.gif")
    models["triangle"] = Model((-0.01, -0.01, 0.01, -0.01, 0.0, 0.01), (1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1))

    physics_bodies["background"] = PhysicsBody(models["background"].x, models["background"].y, models["background"].width, models["background"].height, moving = False)
    physics_bodies["background1"] = PhysicsBody(models["background1"].x, models["background1"].y, models["background1"].width, models["background1"].height, moving = False)
    physics_bodies["background2"] = PhysicsBody(models["background2"].x, models["background2"].y, models["background2"].width, models["background2"].height, moving = False)
    physics_bodies["background3"] = PhysicsBody(models["background3"].x, models["background3"].y, models["background3"].width, models["background3"].height, moving = False)
    physics_bodies["background4"] = PhysicsBody(models["background4"].x, models["background4"].y, models["background4"].width, models["background4"].height, moving = False)
    physics_bodies["background5"] = PhysicsBody(models["background5"].x, models["background5"].y, models["background5"].width, models["background5"].height, moving = False)
    physics_bodies["background6"] = PhysicsBody(models["background6"].x, models["background6"].y, models["background6"].width, models["background6"].height, moving = False)
    physics_bodies["background7"] = PhysicsBody(models["background7"].x, models["background7"].y, models["background7"].width, models["background7"].height, moving = False)
    physics_bodies["background8"] = PhysicsBody(models["background8"].x, models["background8"].y, models["background8"].width, models["background8"].height, moving = False)
    physics_bodies["player"] = PhysicsBody(models["player"].x, models["player"].y, models["player"].width, models["player"].height)


    print("loaded the scene")
