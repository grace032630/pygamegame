import pygame
from game2.controller2 import GameControl2
from game2.model2 import GameModel2
from game2.view2 import GameView2
from game2.game2 import Game2
import os
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT, FPS,IMAGE_PATH,SOUND_PATH
pygame.init()



class Map2:
    def __init__(self):
        # win
        self.map_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "bigmapnew2.png")), (WIN_WIDTH, WIN_HEIGHT))
        # button
        #self.level1_btn = Buttons(70, 230, 90, 90)  # x, y, width, height
        self.level2_btn = Buttons(390, 175, 100, 100)
        #self.level3_btn = Buttons(710, 250, 90, 90)
        self.sound_btn = Buttons(725, 525, 90, 70)
        self.mute_btn = Buttons(830, 525, 90, 70)
        self.buttons = [self.level2_btn,self.sound_btn,self.mute_btn]#self.level1_btn,self.level3_btn,
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "click.mp3"))
    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "music.mp3"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.2)
    def map_run2(self):
        map_run2 = True
        clock2 = pygame.time.Clock()
        pygame.display.set_caption("Covid-19 Defense Game-map2")
        self.play_music()
        while map_run2:
            clock2.tick(FPS)
            self.map_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    map_run2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.level2_btn.clicked(x, y):
                        self.sound.play()
                        pygame.quit()
                        game = Game2()
                        game.run2()
                        map_run2 = False  
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
            pygame.draw.rect(win, WHITE, self.frame, 12)
