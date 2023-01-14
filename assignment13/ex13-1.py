import random
import arcade


class Panda(arcade.Sprite):
    def __init__(self,game):
        super().__init__("assignment13\images\PoPanda.png")
        self.center_x= game.width//4*3
        self.center_y= 80
        self.width=106 # dimension of object
        self.height=150
        self.speed=8

class Tiger(arcade.Sprite):
    def __init__(self,game):
        super().__init__("assignment13\images\_tiger.png")
        self.center_x= game.width//4
        self.center_y= 80
        self.width=145 # dimension of object
        self.height=131
        self.speed=8

class Tai_lung(arcade.Sprite):
    def __init__(self,game):
        super().__init__("assignment13\images\Tai-Lung-2-icon.png")
        self.center_x=random.randint(0,game.width)
        self.center_y=game.height+100
        self.angle=-45
        self.width=200
        self.height=200
        self.speed=1.5

class Shen(arcade.Sprite):
    def __init__(self,game):
        super().__init__("assignment13\images\Lord_Shen.png")
        self.center_x=random.randint(0,game.width)
        self.center_y=game.height+25
        self.angle=45
        self.width=300
        self.height=75
        self.speed=1.5

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar Game 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background= arcade.load_texture("assignment13\images\_bg.jpg")
        self.po=Panda(self)
        self.tiger=Tiger(self)
        self.tielang=Tai_lung(self)
        self.shen=Shen(self)

    # نمایش
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)

        self.po.draw()
        self.tiger.draw()
        self.tielang.draw()
        self.shen.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # print("yek dokme feshar dade shode")
        if symbol==97: # po to left
            self.po.center_x -=self.po.speed
        elif symbol==100:  # po to right
            self.po.center_x +=self.po.speed
        elif symbol==symbol==arcade.key.K: # tiger to left
            self.tiger.center_x -=self.tiger.speed
        elif symbol==symbol==arcade.key.L: # tiger to right
            self.tiger.center_x +=self.tiger.speed

    def on_update(self, delta_time: float):
        self.tielang.center_y -=self.tielang.speed
        self.shen.center_y -=self.shen.speed

window=Game()
arcade.run()