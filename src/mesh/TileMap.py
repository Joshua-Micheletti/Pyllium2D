import pyglet

class TileMap():

    def __init__(self):
        self.images = []
        self.texture = None
        self.width = 0
        self.height = 0


    def load_tilemap(self, path, width, height):
        self.width = width
        self.height = height
        self.texture = pyglet.image.load(path)

        image_width = self.texture.width
        image_height = self.texture.height

        tile_width = image_width / width
        tile_height = image_height / height

        print(f"tile_size: ({tile_width}, {tile_height})")

        for i in range(width):
            self.images.append([])
            for j in range(height):
                tile_image = self.texture.get_region(int(i * tile_width), int(j * tile_height), int(tile_width), int(tile_height))
                self.images[len(self.images) - 1].append(tile_image)

    def get_by_index(self, index):
        column = int(index / self.width)
        row = index % self.width
        return(self.images[row][(self.height - 1) - column])
