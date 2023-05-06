class Entity:

    def __init__(self, model = "", body = ""):
        self.states = dict()
        self.model = model
        self.body = body
        self.movement_speed_threshold = 0.4

    def update(self, model = "", body = ""):
        pass


class Player(Entity):

    def __init__(self, model = "", body = ""):
        super().__init__(model, body)

        self.states["moving"] = False
        self.states["airborne"] = False
        self.states["crouching"] = False
        self.states["right"] = True
        self.states["rising"] = False
        self.states["midair"] = False
        self.states["falling"] = False

        self.current_animation = -1
        self.current_right = True

    def update(self, model, body):
        if body.speed[0] < self.movement_speed_threshold and body.speed[0] > -self.movement_speed_threshold:
            self.states["moving"] = False
        else:
            self.states["moving"] = True

        if not body.touching["down"]:
            self.states["airborne"] = True
            if body.speed[1] > 2:
                self.states["rising"] = True
                self.states["midair"] = False
                self.states["falling"] = False
            elif body.speed[1] < 2 and body.speed[1] > -2:
                self.states["rising"] = False
                self.states["midair"] = True
                self.states["falling"] = False
            elif body.speed[1] < -2:
                self.states["rising"] = False
                self.states["midair"] = False
                self.states["falling"] = True
        else:
            self.states["airborne"] = False
            self.states["rising"] = False
            self.states["midair"] = False
            self.states["falling"] = False


        if body.speed[0] > 0:
            self.states["right"] = True

        if body.speed[0] < 0:
            self.states["right"] = False

        self.update_animation(model)

    def update_animation(self, model):
        right = not self.states["right"]

        if self.states["airborne"]:
            if self.states["rising"]:
                model.play_animation(7, right)
            elif self.states["midair"]:
                model.play_animation(6, right)
            elif self.states["falling"]:
                model.play_animation(5, right)
        else:
            if self.states["crouching"]:
                if self.states["moving"]:
                    model.play_animation(0, right)
                else:
                    model.play_animation(1, right)
            else:
                if self.states["moving"]:
                    model.play_animation(8, right)
                else:
                    model.play_animation(9, right)
