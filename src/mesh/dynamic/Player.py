from model.dynamic.DynamicSprite import DynamicSprite

class Player(DynamicSprite):

    def __init__(self, path, group):

        self.states = dict()
        self.states["moving"] = False
        self.states["airborne"] = False
        self.states["crouching"] = False
        self.states["right"] = True
        self.states["rising"] = False
        self.states["midair"] = False
        self.states["falling"] = False

        self.current_animation = -1
        self.current_right = True

        DynamicSprite.__init__(self, path, group)

    def update_state(self, body):

        if body.speed[0] < 0.1 and body.speed[0] > -0.1:
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

        self.update_animation()

    def update_animation(self):
        if self.states["airborne"]:
            if self.states["rising"]:
                self.set_animation(7)
            elif self.states["midair"]:
                self.set_animation(6)
            elif self.states["falling"]:
                self.set_animation(5)
        else:
            if self.states["crouching"]:
                if self.states["moving"]:
                    self.set_animation(0)
                else:
                    self.set_animation(1)
            else:
                if self.states["moving"]:
                    self.set_animation(8)
                else:
                    self.set_animation(9)

    def set_animation(self, animation_index):

        if animation_index == self.current_animation and self.states["right"] == self.current_right:
            return(False)

        if self.states["right"] == True:
            self.sprite.image = self.animations[animation_index]
            self.current_right = True
        else:
            self.sprite.image = self.animations[animation_index].get_transform(flip_x = True)
            self.current_right = False

        self.current_animation = animation_index


    def place(self, x, y):
        self.sprite.update(x + self.sprite.width / 2, y + self.sprite.height / 2)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.center = (self.sprite.x, self.sprite.y)

        self.bounding_box.x = self.x - self.sprite.width / 2
        self.bounding_box.y = self.y - self.sprite.height / 2
