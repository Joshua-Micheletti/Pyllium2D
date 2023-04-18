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
    # models["background"].scale(10)
    models["player"] = Sprite("../res/animation/growlithe.gif", groups["foreground"])
    # models["goldeen"] = Sprite("../res/animation/goldeen.gif")
    models["triangle"] = Model((-0.01, -0.01, 0.01, -0.01, 0.0, 0.01), (1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1))

    physics_bodies["background"] = PhysicsBody(models["background"].x, models["background"].y, models["background"].width, models["background"].height, moving = False)
    physics_bodies["player"] = PhysicsBody(models["player"].x, models["player"].y, models["player"].width, models["player"].height)


    print("loaded the scene")
