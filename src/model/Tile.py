from shared import batch
import pyglet

class Tile:
    def __init__(self, image, group):
        self.sprite = pyglet.sprite.Sprite(image, batch = batch, group = group)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.width = self.sprite.width
        self.height = self.sprite.height

    def move(self, x, y):
        self.sprite.update(self.sprite.x + x, self.sprite.y + y)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.width = self.sprite.width
        self.height = self.sprite.height

    def place(self, x, y):
        self.sprite.update(x, y)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.width = self.sprite.width
        self.height = self.sprite.height

    def scale(self, amount):
        self.sprite.update(scale = amount)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.width = self.sprite.width
        self.height = self.sprite.height
