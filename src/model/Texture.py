from OpenGL.GL import *
from PIL import Image

class Texture:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.texture = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

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
        
    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)