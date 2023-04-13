from shared import batch
from termcolor import colored
import pyglet

class Sprite:
    def __init__(self):
        self.texture = None
        self.sprite = None

    def __init__(self, path):
        self.texture = None
        self.sprite = None
        self.load_texture(path)

    def load_texture(self, path):
        try:
            self.texture = pyglet.image.load(path)
            self.sprite = pyglet.sprite.Sprite(self.texture, batch = batch)
        except Exception as e:
            print(colored("Failed to load image"), "red")
            print(colored(e, "red"))
