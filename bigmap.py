import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from game.game import Game
#from game2.game2 import Game2
#from game3.game3 import Game3
import os
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT,FPS,IMAGE_PATH,SOUND_PATH
pygame.init()
import math


class Map:    
    def __init__(self):
        # win
        self.map_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background        
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "bigmapnew1.png")), (WIN_WIDTH, WIN_HEIGHT))
        # button
        self.level1_btn = Buttons(700, 210, 100, 100)  # x, y, width, height
        self.sound_btn = Buttons(725, 525, 90, 70)
        self.mute_btn = Buttons(830, 525, 90, 70)
        self.buttons = [self.level1_btn,self.sound_btn,self.mute_btn]
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "click.mp3"))

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "music.mp3"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.2)

    def draw_be(self):
        self.map_win.blit(BEFORE_IMAGE, (0, 0))

    def map_run(self):
        map_run = True
        pygame.display.set_caption("Covid-19 Defense Game-map1")
        self.play_music()
        clock = pygame.time.Clock()
        while map_run:
            clock.tick(FPS)
            self.map_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    map_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.level1_btn.clicked(x, y):
                        self.sound.play()
                        pygame.quit()
                        game = Game()
                        game.run()
                        map_run = False
                    if self.mute_btn.clicked(x, y):
                        self.sound.play()
                        pygame.mixer.music.pause()   
                    if self.sound_btn.clicked(x, y):
                        self.sound.play()
                        pygame.mixer.music.unpause()
                                         
            for i in self.buttons:
                i.create_frame(x,y)
                i.draw_frame(self.map_win)
                pygame.display.update()
        pygame.quit()
class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

    def create_frame(self, x: int, y: int):
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win,WHITE, self.frame, 12)
