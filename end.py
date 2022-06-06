import pygame
import os
from settings import WIN_WIDTH, WIN_HEIGHT, END_IMAGE,IMAGE_PATH,SOUND_PATH
from color_settings import *
import math
import sys
from pygame.locals import *
import time


class end1:
    def __init__(self):
        # win
        self.end_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 改
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "end1.png")), (WIN_WIDTH, WIN_HEIGHT))
        self.end_btn = Buttons(76, 437, 180, 120)
        self.sound_btn = Buttons(725, 525, 90, 70)
        self.mute_btn = Buttons(830, 525, 90, 70)
        self.buttons = [self.end_btn, self.sound_btn, self.mute_btn]  # self.level1_btn,self.level3_btn,
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "sound.flac"))

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "music.mp3"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.2)

    def end_run1(self):
        end_run1 = True
        pygame.display.set_caption("Covid-19 Defense Game-END1")
        clockend = pygame.time.Clock()
        self.play_music()
        if end_run1 == True:
            names = locals()  # locals() 函数会以字典类型返回当前位置的全部局部变量
            animates = []
            for i in range(1, 9):
                names['end_image%s' % i] = pygame.transform.scale(
                    pygame.image.load(os.path.join(IMAGE_PATH, "end%s.png" % i)), (WIN_WIDTH, WIN_HEIGHT))
                animates.append(names['end_image%s' % i])
            for i in range(0, 8):
                self.trailer_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
                self.end_win.blit(animates[i], (0, 0))
                pygame.time.wait(1000)
                pygame.display.update()
            pygame.time.wait(10000)
            pygame.quit()
            sys.exit()
            self.end_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
            self.bg = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "end8.png")),
                                             (WIN_WIDTH, WIN_HEIGHT))
            self.end_btn = Buttons(76, 437, 180, 120)
            self.sound_btn = Buttons(725, 525, 90, 70)
            self.mute_btn = Buttons(830, 525, 90, 70)
            self.buttons = [self.end_btn, self.sound_btn, self.mute_btn]
            self.sound = pygame.mixer.Sound("./sound/sound.flac")
            x, y = pygame.mouse.get_pos()
            self.end_win.blit(END_IMAGE, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.end_btn.clicked(x, y):
                        self.sound.play()
                        pygame.quit()
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()
                    if self.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()
            for i in self.buttons:
                i.create_frame(x, y)
                i.draw_frame(self.end_win)  #
                pygame.display.update()

        # pygame.quit()


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
