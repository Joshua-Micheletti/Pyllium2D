from OpenGL.GL import *
from PIL import Image

class Texture:
    def __init__(self, path = ""):
        self.width = 0
        self.height = 0
        self.texture = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        if len(path) != 0:
            self.load_image(path)

    def load_image(self, path):
        image = Image.open(path)
        convert = image.convert("RGBA")
        image_data = convert.transpose(Image.FLIP_TOP_BOTTOM).tobytes()
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
                image_data)       # data to load as texture
        
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

        if len(path) != 0 and rows != 0 and columns != 0:
            self.load_image_sheet(path, rows, columns)

    def load_image_sheet(self, path, rows, columns):
        super().load_image(path)

        self.rows = rows
        self.columns = columns

        self.tile_width = self.width / self.columns
        self.tile_height = self.height / self.rows
        self.tile_uv_width = 1 / self.columns
        self.tile_uv_height = 1 / self.rows
        

    def get_uv(self, row, column):
        return((column / self.columns, row / self.rows))
    
    def get_size(self):
        return((self.tile_width, self.tile_height))
    
    def get_total_size(self):
        return((self.width, self.height))