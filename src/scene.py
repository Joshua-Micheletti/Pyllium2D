from shared import models
from shared import batch
import pyglet
from model.Model import Model
from model.Sprite import Sprite

def load_scene():
    global models
    global batch
    
    models["car"] = Sprite("../res/texture/test.png")
    models["gally"] = Sprite("../res/texture/gally5.png")
    models["triangle"] = Model((-0.01, -0.01, 0.01, -0.01, 0.0, 0.01), (1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1))
    print("loaded the scene")
