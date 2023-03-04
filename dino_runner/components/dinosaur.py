import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING,DUCKING

class Dinosaur(Sprite):
    Pos_X = 80
    Pos_Y = 310
    Pos_Yp = 350
    Pos_YJ = 300

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.Pos_X
        self.dino_rect.y = self.Pos_Y

        self.step_index = 0

    def update(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.duck()
        elif user_input[pygame.K_SPACE]:
            self.jupm()
        else:
            self.run()

        if self.step_index >= 10:
           self.step_index = 0

        
        

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)


    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING [1]
            

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.Pos_X
        self.dino_rect.y = self.Pos_Y
        self.step_index += 1

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING [1]
            

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.Pos_X
        self.dino_rect.y = self.Pos_Yp
        self.step_index += 1


        