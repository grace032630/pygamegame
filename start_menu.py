import pygame
import os
from game.game import Game
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT#, FPS
from trailer import Trailer
from settings import IMAGE_PATH,SOUND_PATH
pygame.init()
pygame.mixer.init()


class StartMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "startmenu.jpg")), (WIN_WIDTH, WIN_HEIGHT))
        self.start = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "start.png")), (280, 200))
        self.exit = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "exit.png")), (180, 150))
        self.soundon = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "soundon.png")), (70, 70))
        self.mute = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "mute.png")), (70, 70))
        # button
        self.start_btn = Buttons(372, 250, 280, 100)  # x, y, width, height
        self.exit_btn = Buttons(422, 385, 180, 78)
        self.sound_btn = Buttons(430, 25, 75, 70)
        self.mute_btn = Buttons(520, 25, 75, 70)
        self.buttons = [self.sound_btn,
                        self.mute_btn,
                        self.start_btn,
                        self.exit_btn]
        # music and sound
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "sound.flac"))

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "music.mp3"))
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.1)

    def menu_run(self):
        run = True
        #clock = pygame.time.Clock()
        pygame.display.set_caption("Covid-19 Defense Game")
        self.play_music()
        while run:
            #clock.tick(FPS)
            self.menu_win.blit(self.bg, (0, 0))
            self.menu_win.blit(self.start, (372, 200))
            self.menu_win.blit(self.exit, (422, 350))
            self.menu_win.blit(self.mute, (522, 25))
            self.menu_win.blit(self.soundon, (432, 25))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.start_btn.clicked(x, y):
                        self.sound.play()
                        trailer=Trailer()
                        trailer.trailer_run()
                        #bigmap = Map()
                        #bigmap.map_run()
                        run = False
                    # 播放
                    if self.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()
                    # 暫停
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()
                    if self.exit_btn.clicked(x, y):
                        pygame.quit()
                        exit()

            # while cursor is moving (not click)
            # use a for loop to go through all the buttons, create the frame, and draw it.
            for bu in self.buttons:
                bu.create_frame(x, y)
                bu.draw_frame(self.menu_win)

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
        """if cursor position is on the button, create button frame"""
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 10)
