import arcade

class Heart(arcade.Sprite):
    def __init__(self,i):
        super().__init__("images\heart.png")
        self.center_x=25*(i+1)
        self.center_y=20
        self.width=20
        self.height=20
        