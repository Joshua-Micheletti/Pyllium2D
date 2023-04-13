from shared import models
from shared import batch
import pyglet
from model.Model import Model
from model.Sprite import Sprite

def load_scene():
    global models
    global batch
    
    models["car"] = Sprite("../res/texture/test.png")
    models["triangle"] = Model((-0.5, -0.5, 0.5, -0.5, 0.0, 0.5), (1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1))
