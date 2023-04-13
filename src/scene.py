from shared import models
from shared import batch
import pyglet
from model.Model import Model

def load_scene():
    global models
    global batch
    car_image = pyglet.image.load('../res/texture/test.png')
    models["car"] = pyglet.sprite.Sprite(car_image, batch = batch)
    models["triangle"] = Model((-0.5, -0.5, 0.5, -0.5, 0.0, 0.5), (1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1))
