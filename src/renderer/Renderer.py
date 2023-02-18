from pyglet.gl import *
import pyglet
from shared import models

class Renderer():
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

    def loadModelsIntoBatch(self):
        global models
        car_image = pyglet.image.load('./renderer/test.png')
        models["car"] = pyglet.sprite.Sprite(car_image, batch = self.batch)
       
    def render(self):
        self.batch.draw()


