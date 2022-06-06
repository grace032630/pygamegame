import pygame
import os
from settings import WIN_WIDTH, WIN_HEIGHT,IMAGE_PATH,SOUND_PATH
from color_settings import *
import math
import sys
from pygame.locals import *
from bigmap import Map
import time
pygame.init()
pygame.mixer.init()


 
class Trailer:
    def __init__(self):
        # win
        self.trailer_win=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.skip_btn = Buttons(76, 437, 180,120)
        self.sound_btn = Buttons(725, 525, 90, 70)
        self.mute_btn = Buttons(830, 525, 90, 70)
        self.buttons = [self.skip_btn,self.sound_btn,self.mute_btn]
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "sound.flac"))
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "music.mp3"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.2)
    def trailer_run(self):        
        trailer_run = True
        pygame.display.set_caption("Covid-19 Defense Game-trailer")       
        self.play_music()        
        while trailer_run:           
            self.trailer_win=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
            names = locals()
            animates=[]
            for i in range(1,9):
                names['bg_image%s'%i] = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH,"be%s.png"%i)),(WIN_WIDTH, WIN_HEIGHT)).convert()
                animates.append(names['bg_image%s'%i])
            for j in range(0,8):
                self.trailer_win=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
                self.trailer_win.blit(animates[j], (0, 0))
                time.sleep(2.5)
                pygame.display.update()
            trailer_run = False
            bigmap = Map()
            bigmap.map_run()            
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    trailer_run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.skip_btn.clicked(x, y):
                        self.sound.play()
                        trailer_run= False
                        pygame.init()
                        bigmap = Map()
                        bigmap.map_run()
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()   
                    if self.sound_btn.clicked(x, y):
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
            pygame.draw.rect(win, WHITE, self.frame, 20)

