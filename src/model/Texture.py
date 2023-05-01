from OpenGL.GL import *
from PIL import Image

class Texture:
    def __init__(self, path = ""):
        self.width = 0
        self.height = 0
        self.texture = glGenTextures(1)
        self.image_data = None
        self.convert = None

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        if len(path) != 0:
            self.load_image(path)

    def load_image(self, path):
        image = Image.open(path)
        self.convert = image.convert("RGBA")
        self.image_data = self.convert.transpose(Image.FLIP_TOP_BOTTOM).tobytes()
        self.width = image.width
        self.height = image.height
        image.close()

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(
                GL_TEXTURE_2D,    # where to load texture data
                0,                # mipmap level
                GL_RGBA8,         # format to store data in
                self.width,       # image dimensions
                self.height,      #
                0,                # border thickness
                GL_RGBA,          # format data is provided in
                GL_UNSIGNED_BYTE, # type to read data as
                self.image_data)  # data to load as texture

    def get_size(self):
        return((self.width, self.height))

    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)


class TextureSheet(Texture):

    def __init__(self, path = "", rows = 0, columns = 0):
        super().__init__()

        self.tile_width = 0
        self.tile_height = 0
        self.tile_uv_width = 0
        self.tile_uv_height = 0
        self.rows = 0
        self.columns = 0
        self.valid_tiles = []

        if len(path) != 0 and rows != 0 and columns != 0:
            self.load_image_sheet(path, rows, columns)

    def load_image_sheet(self, path, rows, columns):
        super().load_image(path)

        self.rows = rows
        self.columns = columns

        self.tile_width = int(self.width / self.columns)
        self.tile_height = int(self.height / self.rows)

        alpha = self.convert.split()[-1]
        alpha_values = alpha.load()

        for row in range(self.rows):
            for column in range(self.columns):
                found = False
                for pixel_y in range(self.tile_height):
                    for pixel_x in range(self.tile_width):
                        if alpha_values[column * self.tile_width + pixel_x, row * self.tile_height + pixel_y] != 0:
                            found = True

                if found:
                    self.valid_tiles.append((self.rows - row - 1, column))

        self.tile_uv_width = 1 / self.columns
        self.tile_uv_height = 1 / self.rows


    def get_uv(self, row, column):
        if (row, column) in self.valid_tiles:
            return((column / self.columns, row / self.rows))
        else:
            return(False)

    def get_size(self):
        return((self.tile_width, self.tile_height))

    def get_total_size(self):
        return((self.width, self.height))
