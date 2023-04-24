from pyglet.gl import *
import pyglet
from shared import models
from shared import cameras
from shared import batch
from shared import groups
from shared import *
from model.Model import Model
from model.dynamic.DynamicSprite import DynamicSprite
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

        bodies = get_physics_world().physics_bodies

        for name in bodies.keys():
            if name in models.keys():
                models[name].place(bodies[name].x, bodies[name].y)

        for name in models.keys():
            if isinstance(models[name], DynamicSprite):
                models[name].update_state(bodies[name])

        with cameras["world"]:
            batch.draw()
