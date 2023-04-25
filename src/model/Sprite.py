from shared import batch
from shared import groups
from termcolor import colored
import pyglet
from pyglet import shapes
from struct import unpack

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
        self.animation_sequence = None
        self.texture_bin = None
        self.source = path
        self.animations = []

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
            self.texture_bin = pyglet.image.atlas.TextureBin()
            self.texture.add_to_texture_bin(self.texture_bin)
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

    def load_sprite_sheet(self, path, rows, columns, group):
        try:
            self.texture = pyglet.image.load(path)
            self.texture_bin = pyglet.image.atlas.TextureBin()
            self.animation_sequence = pyglet.image.ImageGrid(self.texture, rows, columns)

            self.animations = []

            frames = []

            for i in range(rows):
                for j in range(columns):
                    rawimage = self.animation_sequence[(i, j)].get_image_data()
                    format = 'RGBA'
                    pitch = rawimage.width * len(format)
                    pixels = rawimage.get_data(format, pitch)

                    data = unpack("%iB" % (4 * self.animation_sequence[(i, j)].width * self.animation_sequence[(i, j)].height), pixels)
                    mask = data[3::4]

                    valid_frame = False

                    for value in mask:
                        if value != 0:
                            valid_frame = True

                    if valid_frame:
                        frames.append(pyglet.image.AnimationFrame(self.animation_sequence[(i, j)], duration = 0.2))

                self.animations.append(pyglet.image.Animation(frames = frames))
                self.animations[len(self.animations) - 1].add_to_texture_bin(self.texture_bin)
                frames = []

            self.sprite = pyglet.sprite.Sprite(img = self.animations[rows - 8], batch = batch, group = group)
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

            self.set_anchor()

        except Exception as e:
            print(colored("Failed to load image", "red"))
            print(colored(e, "red"))

    def load_texture_region(self, path, group, area_x, area_y, area_w, area_h):
        try:
            self.texture = pyglet.image.load(path)
            self.texture = self.texture.get_region(area_x, area_y, area_w, area_h)
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


    def set_anchor(self):
        """Set anchor points for animation. Anchor point is set for each individual frame image."""
        if len(self.animations) != 0:
            for animation in self.animations:
                for f in animation.frames:
                    f.image.anchor_x = f.image.width / 2
                    f.image.anchor_y = f.image.height / 2

        self.texture.anchor_x = self.texture.width / 2



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
