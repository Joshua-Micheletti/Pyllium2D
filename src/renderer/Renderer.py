from pyglet.gl import *
import pyglet
from shared import models
from shared import cameras
from shared import batch
from shared import groups
from model.Model import Model
from pyglet.graphics.shader import Shader, ShaderProgram

class Renderer():
    def __init__(self):
        print("new renderer")
        groups["background"] = pyglet.graphics.Group(order = 0)
        groups["foreground"] = pyglet.graphics.Group(order = 1)
        groups["debug"] = pyglet.graphics.Group(order = 2)
        groups["debug"].visible = False

    def render(self):
        global batch
        global cameras

        with cameras["world"]:
            batch.draw()
            
