from model.Model import Model
import time

class Frame():
    def __init__(self, u = 0, v = 0, t = 0):
        self.u = u
        self.v = v
        self.t = t

    def set_uv(self, u, v):
        self.u = u
        self.v = v

    def set_duration(self, t):
        self.t = t


class Animation(Model):
    def __init__(self, mesh = "", texture = "", shader = "", body = "", mesh_obj = None, texture_obj = None):
        super().__init__(mesh, texture, shader, body, mesh_obj, texture_obj)

        self.mesh_obj = mesh_obj
        self.texture_obj = texture_obj
        self.frames = []
        self.current_animation = 0
        self.current_frame = 0
        self.last_update = time.time()
        self.flipped_x = False

        for i in range(texture_obj.rows):
            self.frames.append([])
            for j in range(texture_obj.columns):
                uvs = texture_obj.get_uv(i, j)

                if uvs is not False:
                    self.frames[i].append(Frame(uvs[0], uvs[1], 0.2))

        self.play_animation(0)

    def play_animation(self, index, flipped_x = False):
        if self.current_animation == index and flipped_x == self.flipped_x:
            return

        self.flipped_x = flipped_x
        self.current_animation = index
        self.current_frame = 0
        self.last_update = time.time() - self.frames[self.current_animation][self.current_frame].t

    def update(self):
        current_time = time.time()
        current_frame_obj = self.frames[self.current_animation][self.current_frame]

        if current_time > self.last_update + current_frame_obj.t:
            self.mesh_obj.set_uv(current_frame_obj.u, current_frame_obj.v, self.texture_obj.tile_uv_width, self.texture_obj.tile_uv_height, flipped_x = self.flipped_x)
            self.last_update = time.time()
            self.current_frame = (self.current_frame + 1) % len(self.frames[self.current_animation])
