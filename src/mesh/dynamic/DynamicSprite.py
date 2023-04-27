from model.Sprite import Sprite

class DynamicSprite(Sprite):

    def __init__(self, path, group):
        print("new dynamic sprite")

        Sprite.__init__(self, path, group)

        def update_state(self, body):
            pass
