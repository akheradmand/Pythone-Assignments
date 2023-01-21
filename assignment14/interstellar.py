# import random
import time
import arcade
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar Game 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background= arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.spaceship=Spaceship(self)
        self.enemy_list=[]
        self.time=time.time()
        self.heart_number=3
        self.heart_list=[Heart(self.heart_number-1-i) for i in range(self.heart_number)] #اندیس برای حذف قلبهااز راست به چپ
        self.game_over=False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)

        self.spaceship.draw()

        for enemy in self.enemy_list:
            enemy.draw()

        for bullet in self.spaceship.bullet_list:
            bullet.draw()

        for heart in self.heart_list:
            heart.draw()

        arcade.draw_text(self.spaceship.score,self.width*9//10,15,arcade.color.RED,15)

        if self.game_over==True:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over",self.width//3,self.height//2,arcade.color.RED,40)
            arcade.play_sound(arcade.load_sound(":resources:sounds/gameover5.wav"))

        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.LEFT:
            self.spaceship.change_x=-1
        elif symbol==arcade.key.RIGHT:
            self.spaceship.change_x=1
        elif symbol==arcade.key.DOWN or self.game_over==True:
            self.spaceship.change_x=0
        elif symbol==arcade.key.SPACE and self.game_over==False:
            self.spaceship.fire()
            arcade.play_sound(arcade.load_sound(":resources:sounds/hit2.wav"))
        
    # def on_key_release(self, symbol: int, modifiers: int):
    #     self.spaceship.change_x=0

    def on_update(self, delta_time: float):

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.spaceship,enemy):
                self.game_over=True
        
        for enemy in self.enemy_list:
            for bullet in self.spaceship.bullet_list:
                if arcade.check_for_collision(enemy,bullet):
                    arcade.play_sound(arcade.load_sound(":resources:sounds/explosion2.wav"))
                    self.enemy_list.remove(enemy)
                    self.spaceship.bullet_list.remove(bullet)
                    self.spaceship.score += 1

        self.spaceship.move()

        for enemy in self.enemy_list:
            enemy.move()

        for bullet in self.spaceship.bullet_list:
            bullet.move()

        for enemy in self.enemy_list:
            if enemy.center_y<0:
                for heart in self.heart_list:
                    self.heart_list.remove(heart)
                    break
                    
                self.enemy_list.remove(enemy)
        
        for bullet in self.spaceship.bullet_list:
            if bullet.center_y>self.height:
                self.spaceship.bullet_list.remove(bullet)

        delta_time=round((time.time()-self.time),0)
        # print(round((time.time()-self.time),2))
        if delta_time==3 and self.game_over==False:
            self.time=time.time()
            self.new_enemy=Enemy(self)
            self.enemy_list.append(self.new_enemy)

        if len(self.heart_list)==0:
            self.game_over=True

window=Game()
arcade.run()