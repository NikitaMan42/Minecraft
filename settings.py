from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

H_B = 8         # высота блока стены
H_COKOL = 2     # высота цоколя
H_ZONA_A = 2    # высота зоны А
W_B_1 = 9       # ширина блока стены тип 1
W_B_2 = 7       # ширина блока стены тип 2

W_OKNA_1, H_OKNA_1 = 5, 5       # ширина и высота окна типа 1
W_OKNA_2, H_OKNA_2 = 4, 5       # ширина и высота окна типа 2
W_OKNA_3, H_OKNA_3 = 2, 5       # ширина и высота окна типа 3 - лестничные площадки
W_OKNA_4, H_OKNA_4 = 1, 2       # ширина и высота окна типа 4 - вентиляция

AIR = 0                 # воздух
STONE = 1               # камень для основы
WHITE = 155
BROWN = 35, 14          # было 159,12
ORANGE = 159,1
BROWN_DARK = 159,12      # темно-коричневый для цоколя было 159,7
OKNO = 160      # 102              тонкое окно
PAUSE = 0.01

mc = Minecraft.create()

posMAIN = Vec3(122, 67, -1011)
# posMAIN = Vec3(488, 73, -744)
''' для первичного позиционирования игрока в новом мире разкомментарить
posMy = posMAIN.clone()
posMy.y += 5
mc.player.setTilePos(posMy)
#'''
