from pyglet.gl import *
import pyglet
from shared import models
from shared import cameras
from shared import batch
from model.Model import Model
from pyglet.graphics.shader import Shader, ShaderProgram

class Renderer():
    def __init__(self):
        print("new renderer")

    def render(self):
        global batch
        # global cameras

        # with cameras["world"]:
        batch.draw()
        # models["triangle"].draw(GL_TRIANGLES)
