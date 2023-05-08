from shared import *
from entity.Entity import Entity

class Tilemap:

    def __init__(self, width = 0, height = 0, texture_sheet = "", tile_size = 64):
        self.cells = []
        self.width = width
        self.height = height
        self.centered = False
        self.texture_sheet = texture_sheet
        self.tile_size = tile_size

        self.initialize(self.width, self.height)


    def initialize(self, width = 0, height = 0):
        if (width == 0 or height == 0) and (self.width == 0 or self.height == 0):
            return(False)

        self.cells = []

        for i in range(height):
            self.cells.append([])
            for j in range(width):
                self.cells[i].append(-1)


    def add_structure(self, str_cells, x, y):
        structure_height = len(str_cells)
        structure_width = len(str_cells[0])

        if structure_width + x > self.width or structure_height + y > self.height:
            return(False)

        for i in range(structure_height):
            for j in range(structure_width):
                self.cells[i][j] = str_cells[i][j]


    def create_tiles(self):
        rm = get_resource_manager()
        pw = get_physics_world()

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j] != -1:
                    uvs = rm.textures[self.texture_sheet].get_index_uv(self.cells[i][j])
                    if uvs != False:
                        id = str(i) + "_" + str(j) + "_" + str(self)

                        rm.add_mesh("tile_mesh_" + id, "square").set_uv(uvs[0], uvs[1], rm.textures[self.texture_sheet].tile_uv_width, rm.textures[self.texture_sheet].tile_uv_height)
                        rm.add_model("tile_" + id, "static", "tile_mesh_" + id, self.texture_sheet, "basic", 1)
                        rm.models["tile_" + id].place(j * self.tile_size, i * self.tile_size)
                        rm.models["tile_" + id].scale_by(4, 4)

                        pw.add_body("tile_" + id, rm.models["tile_" + id].x - rm.models["tile_" + id].width / 2, rm.models["tile_" + id].y - rm.models["tile_" + id].height / 2, rm.models["tile_" + id].width, rm.models["tile_" + id].height, 1, False)
                        entities["tile_entity_" + id] = Entity("tile_" + id, "tile_" + id)
