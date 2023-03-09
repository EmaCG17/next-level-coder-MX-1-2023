import pygame
from dino_runner.utils.constants import (BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_ARIAL)
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.player_hearts.heart_manager import HeartManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacles_manager = ObstacleManager()
        self.heart_manager = HeartManager()
        self.points = 0

    def increase_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacles_manager.update(self.game_speed, self)
        self.increase_score()


    def draw(self):
        self.clock.tick(FPS)
        if self.points < 500:
           self.screen.fill((255, 255, 255))
        else:
            self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        self.draw_score()
        self.obstacles_manager.draw(self.screen)
        self.heart_manager.draw(self.screen)
        self.draw_background()
        if self.heart_manager.heart_count == 1:
            self.draw_final()
        elif self.heart_manager.heart_count == 1 and self.points > 500:
            self.draw_final()
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_ARIAL, 30)
        if self.points < 500:
            surface = font.render("High Score: "+ str(self.points), True, (0,0,0))
        else:
             surface = font.render("High Score: "+ str(self.points), True, (255,255,255))
        rect = surface.get_rect()
        rect.x = 900
        rect.y = 10
        self.screen.blit(surface, rect)

    def draw_final(self):
        font = pygame.font.Font(FONT_ARIAL, 30)
        surface = font.render("Te queda una vida", True, (0,0,0))
       # time = pygame.time.get_ticks() / 1000
        rect = surface.get_rect()
        rect.x = 450
        rect.y = 300
        self.screen.blit(surface, rect)

    

    
                
            