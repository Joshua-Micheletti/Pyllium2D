from pyglet.gl import *
import pyglet
from shared import models
from shared import cameras

class Renderer():
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

    def loadModelsIntoBatch(self):
        global models
        car_image = pyglet.image.load('./renderer/test.png')
        models["car"] = pyglet.sprite.Sprite(car_image, batch = self.batch)
        
        models["triangle"] = pyglet.graphics.vertex_list(2, ('v2f', [-0.5, -0.5,  0.5, -0.5, 0.0,  0.0, 0.5])), ('c3B', [100, 200, 220,  200, 110, 100,  100, 250, 100])
        
       
    def render(self):
        # global cameras
        
        # with cameras["world"]:
        self.batch.draw()
        models["triangle"].draw(GL_TRIANGLES)


