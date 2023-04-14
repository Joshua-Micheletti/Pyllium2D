from shared import cameras

class Controller:

    def __init__(self):
        self.states = dict()
        
        self.states["camera_left"] = False
        self.states["camera_right"] = False
        self.states["camera_up"] = False
        self.states["camera_down"] = False

    def handle_input(self, control):
        if control == "A_down":
            self.states["camera_left"] = True
        if control == "A_up":
            self.states["camera_left"] = False

        if control == "S_down":
            self.states["camera_down"] = True
        if control == "S_up":
            self.states["camera_down"] = False

        if control == "D_down":
            self.states["camera_right"] = True
        if control == "D_up":
            self.states["camera_right"] = False

        if control == "W_down":
            self.states["camera_up"] = True
        if control == "W_up":
            self.states["camera_up"] = False


        if control == "scroll_up":
            cameras["world"].set_zoom(cameras["world"].zoom + 0.1)
        if control == "scroll_down":
            cameras["world"].set_zoom(cameras["world"].zoom - 0.1)

    
    def update(self):
        if self.states["camera_left"] == True:
            cameras["world"].move(-1, 0)
        if self.states["camera_right"] == True:
            cameras["world"].move(1, 0)
        if self.states["camera_up"] == True:
            cameras["world"].move(0, 1)
        if self.states["camera_down"] == True:
            cameras["world"].move(0, -1)