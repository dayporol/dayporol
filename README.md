import pygame
from pygame.constants import APPACTIVE
pygame.init()
import math
import sys
screen = pygame.display.set_mode((400, 600))
bg = pygame.image.load("calc.png")
bg_rect = bg.get_rect()
pygame.display.set_caption("калькулятор от господа боженьки")

displayFont1 = pygame.font.SysFont('arial', 54)
displayFont2 = pygame.font.SysFont('arial', 18)

class Button:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.h = 40
        if name == '0':
            self.w = 70
        else:
            self.w = 40
    def is_pressed(self, xm, ym):
        return abs(self.x-xm) < self.w and abs(self.y - ym) < self.h

buttons = [
    Button ("0", 99, 528),
    Button ("1", 54, 432),
    Button ("2", 153, 432),
    Button ("3", 242, 433),
    Button ("4", 51, 339),
    Button ("5", 151, 338),
    Button ("6", 248, 340),
    Button ("7", 52, 243),
    Button ("8", 155, 243),
    Button ("9", 245, 240),
    Button ("-", 342, 337),
    Button ("+", 340, 432),
    Button ("*", 345, 240),
    Button ("/", 345, 147),
    Button (",", 245, 526),
    Button ("=", 342, 528),
    Button ("%", 245, 147),
    Button ("+/-", 148, 147),
    Button ("AC", 52, 146)]
    

WHITE = 0, 0, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
RED = 255, 0, 0

def find_button(pos):
    x = pos[0]
    y = pos[1]
    for btn in buttons:
        if btn.is_pressed(x,y):
            return btn.name
    print(x,y)
    return ''
acc = 0
op = ''
disp = 0
div=1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            name = find_button(event.pos)
            if '0' <= name <= '9':
                if div == 1:
                    disp = disp*10 + int(name)
                else:
                    disp = disp + int(name)/div
                    div = div * 10
            if name == ',':
                div = 10
            if name in ('+','-','/','*','%'):
                op = name
                acc = disp
                disp = 0
                div = 1
            if name == '=':
                if op == '+':
                    acc += disp
                    disp = acc
                if op == "-":
                    acc -= disp
                    disp = acc
                if op == "*":
                    acc *= disp
                    disp = acc
                if op == "/":
                    acc /= disp
                    disp = acc
                if op == "%":
                    acc = acc / 100 * disp
                    disp = acc
                div = 1
            if name == 'AC':
                acc = 0
                op = ''
                disp = 0
                div = 1
            if name == "+/-":
                disp = -disp
            

    font1 = displayFont1        
    if len(str(disp)) > 9:
        font1 = displayFont2
    digits = font1.render(str(disp), False, (255, 255, 255))
    adigits = displayFont2.render(str(acc), False, (255, 255, 255))
    optext = displayFont2.render(op, False, (255, 255, 255))
 
    screen.blit(bg,bg_rect)
    screen.blit(digits, (20, 10))
    screen.blit(adigits, (30, 70))
    screen.blit(optext, (370, 70))

    pygame.display.flip()
    pygame.time.wait(100)
