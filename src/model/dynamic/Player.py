from model.dynamic.DynamicSprite import DynamicSprite

class Player(DynamicSprite):

    def __init__(self, path, group):

        self.states = dict()
        self.states["moving"] = False
        self.states["airborne"] = False
        self.states["crouching"] = False
        self.states["right"] = True

        self.current_animation = -1
        self.current_right = True

        DynamicSprite.__init__(self, path, group)

    def update_state(self, body):
        if body.speed[0] < 0.01 and body.speed[0] > -0.01:
            self.states["moving"] = False
        else:
            self.states["moving"] = True


        if body.speed[0] > 0:
            self.states["right"] = True

        if body.speed[0] < 0:
            self.states["right"] = False

        print(self.states)
        print(body.speed)
        self.update_animation()

    def update_animation(self):
        if self.states["moving"]:
            self.set_animation(8)
        else:
            self.set_animation(9)

    def set_animation(self, animation_index):
        if animation_index == self.current_animation and self.states["right"] == self.current_right:
                return(False)

        print(self.states["right"])

        if self.states["right"] == True:
            self.sprite.image = self.animations[animation_index]
            self.current_right = True
        else:
            print("flipped")
            self.sprite.image = self.animations[animation_index].get_transform(flip_x = True)
            self.current_right = False


    def place(self, x, y):
        self.sprite.update(x + self.sprite.width / 2, y)
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.center = (self.sprite.x, self.sprite.y + (self.sprite.height / 2))

        self.bounding_box.x = self.x - self.sprite.width / 2
        self.bounding_box.y = self.y
