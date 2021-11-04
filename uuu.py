import pygame
from pygame.constants import WINDOWHITTEST 

pygame.init()

W = 600
H = 400

sc =pygame.display.set_mode((W, H))
pygame.display.set_caption("повтор неудавшегося")
  

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60
pop = 0
ii = YELLOW
clock = pygame.time.Clock()

sp = None

sc.fill(WHITE)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            if pop >= 4:
                pop = 0
            if pop == 0:
                ii = BLUE
            if pop == 1:
                ii = GREEN
            if pop == 2:
                ii = RED
            if pop == 3:
                ii = YELLOW
            pop += 1
            print("кнопка нажата")
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()

        if sp is None:
            sp = pos

        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
        sc.fill(WHITE)
        top = sp[1] if height > 0 else sp[1] + height
        right = sp[0] if width > 0 else sp[0] + width
        width = abs(width)
        height = abs(height)
        pygame.draw.rect(sc, ii, pygame.Rect(right,top,width,height))
        pygame.display.update()
    else:
        sp = None
    clock.tick(FPS)