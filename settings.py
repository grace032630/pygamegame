import pygame
import os

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600
# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)
# enemy path
PATH = [(1010, 475), (994, 500), (971, 525), (952, 541), (932, 553), (902, 550), (879, 532),
        (860, 511), (833, 488), (805, 483), (777, 467), (767, 437), (743, 416), (715, 407),
        (702, 421), (697, 461), (683, 487), (662, 504), (636, 519), (608, 531), (588, 506),
        (566, 484), (532, 457), (518, 471), (495, 504), (464, 520), (439, 484), (425, 456),
        (384, 456), (368, 468), (347, 480), (324, 498), (284, 516), (255, 491), (235, 459), (211, 468),(425,400)]
PATH2 = [(7, 255), (115, 199), (206, 237), (239, 282), (335, 354), (460, 318),(515,400)]
RE_PATH2 = [(1002, 158), (948, 224), (935, 290), (893, 344), (814, 370), (736, 351), (640, 296),(515,400)]
PATH3 = [(9, 203), (45, 206), (84, 212), (120, 220), (156, 229), (191, 238), (227, 251), (261, 263), (297, 269), (337, 268), (375, 264),(445,350)]
RE_PATH3_1 = [(643, 11), (645, 42), (637, 78), (624, 111), (592, 145), (568, 172), (542, 201), (524, 232), (510, 250),(445,350)]
RE_PATH3_2 = [(1008, 237), (958, 242), (907, 251), (862, 262), (825, 271), (792, 285), (750, 304),
              (725, 313), (681, 318), (643, 325), (606, 328), (575, 327), (543, 318), (496, 323),(445,350)]
# base
BASE = pygame.Rect(310, 250, 230, 300)
BASE2 = pygame.Rect(400, 250, 230, 300)
BASE3 = pygame.Rect(330, 200, 230, 300)

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "images")
SOUND_PATH = os.path.join(os.path.dirname(__file__), "sound")
# image
BACKGROUND_IMAGE = pygame.image.load(os.path.join(IMAGE_PATH, "back.png"))
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH,"heart2.png")), (28, 28))
HP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH,"heart.png")), (28, 28))
BOY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "boy.png")), (300, 300))
MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "list.png")), (420, 250))

#前導
BEFORE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "before.gif")), (1024, 600))
TOOL01_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "tool01.png")), (125, 125))
TOOL02_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "tool02.png")), (175, 175))
TOOL03_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "tool03.png")), (180, 180))
ALCOHOL_OP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "alcohol_open.png")), (300, 300))
ALCOHOL_CL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "alcohol_close.png")), (300, 300))
ALCOHOL_OP_RE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "alcohol_open_re.png")), (300, 300))
ALCOHOL_CL_RE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "alcohol_close_re.png")), (300, 300))
# 二三關圖片
BACKGROUND2_IMAGE = pygame.image.load(os.path.join(IMAGE_PATH, "road.png"))
BACKGROUND3_IMAGE = pygame.image.load(os.path.join(IMAGE_PATH, "airport.jpg"))

# 第二關
RING_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "ring.png")), (200, 200))
GLASSES_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "sunglasses.png")), (100, 100))
TAXI_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "taxi.png")), (200, 200))
# 第三關
PASSPORT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "passport.png")), (120, 120))
RESULT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "result.png")), (120, 120))
WEAR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "wear2.png")), (300, 300))
# 靜音
SOUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "soundon.png")), (70, 70))
MUTE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "mute.png")), (70, 70))

JAIL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "jail.png")), (500, 500))
END_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "end8.png")), (1024, 600))