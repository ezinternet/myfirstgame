import pygame,  sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("First Jangil Program")
screen = pygame.display.set_mode((1000, 500))
xpos=50
ypos=50
clock = pygame.time.Clock()
# screen.fill((255, 255, 255))
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    # xpos += 1
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHT]:
        xpos += 1
    if pressed_keys[K_LEFT]:
        xpos -= 1
    if pressed_keys[K_UP]:
        ypos -= 1
    if pressed_keys[K_DOWN]:   # 아래방향이  y축 증가방향이라서
        ypos += 1
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0, 255, 0), (xpos, ypos), 60)
    pygame.display.update()
