from shared import batch
from shared import groups
from termcolor import colored
import pyglet
from pyglet import shapes

class Sprite:
    """Class for creating sprites and displaying images.\n
    Sprite(path)"""

    def __init__(self, path, group):
        self.texture = None
        self.sprite = None
        self.center = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.scale_amount = 1
        self.bounding_box = None

        self.source = path

        directories = path.split("/")

        components = directories[len(directories) - 1].split(".")

        if components[1] == "gif":
            self.load_animation(path, group)
        else:
            self.load_texture(path, group)


    def load_texture(self, path, group):
        try:
            self.texture = pyglet.image.load(path)
            self.sprite = pyglet.sprite.Sprite(self.texture, batch = batch, group = group)
            self.center = (self.sprite.x + (self.sprite.width / 2), self.sprite.y + (self.sprite.height / 2))
            self.x = self.sprite.x
            self.y = self.sprite.y
            self.width = self.sprite.width
            self.height = self.sprite.height
            self.source = path

            self.bounding_box = shapes.BorderedRectangle(self.x, self.y,
                                                         self.width, self.height,
                                                         border = 20,
                                                         border_color = (255, 0, 0, 128),
                                                         color = (0, 0, 0, 128),
                                                         batch = batch, group = groups["debug"])

        except Exception as e:
            print(colored("Failed to load image"), "red")
            print(colored(e, "red"))

    def load_animation(self, path, group):
        try:
            self.texture = pyglet.image.load_animation(path)
            bin = pyglet.image.atlas.TextureBin()
            self.texture.add_to_texture_bin(bin)
            self.sprite = pyglet.sprite.Sprite(img = self.texture, batch = batch, group = group)
            self.center = (self.sprite.x + (self.sprite.width / 2), self.sprite.y + (self.sprite.height / 2))
            self.x = self.sprite.x
            self.y = self.sprite.y
            self.width = self.sprite.width
            self.height = self.sprite.height
            self.source = path

            self.bounding_box = shapes.BorderedRectangle(self.x, self.y,
                                                         self.width, self.height,
                                                         border = 20,
                                                         border_color = (255, 0, 0, 128),
                                                         color = (0, 0, 0, 128),
                                                         batch = batch, group = groups["debug"])

        except Exception as e:
            print(colored("Failed to load animation", "red"))
            print(colored(e, "red"))

    def move(self, x, y):
        self.sprite.update(self.sprite.x + x, self.sprite.y + y)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.center = (self.sprite.x + (self.sprite.width / 2), self.sprite.y + (self.sprite.height / 2))

        self.bounding_box.x = self.x
        self.bounding_box.y = self.y

    def place(self, x, y):
        self.sprite.update(x, y)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.center = (self.sprite.x + (self.sprite.width / 2), self.sprite.y + (self.sprite.height / 2))

        self.bounding_box.x = self.x
        self.bounding_box.y = self.y


    def scale(self, amount):
        self.sprite.update(scale = amount)
        self.scale_amount = amount
        self.width = self.sprite.width
        self.height = self.sprite.height
        self.center = (self.sprite.x + (self.width / 2), self.sprite.y + (self.height / 2))

        self.bounding_box.width = self.width
        self.bounding_box.height = self.height
