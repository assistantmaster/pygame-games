import pygame
import random
import time
import os

pygame.init()

width = 1280 
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("")
#pygame.display.set_icon(pygame.image.load("./images/favicon.png"))

font = pygame.font.Font(None,20)
font2 = pygame.font.Font(None,100)
font3 = pygame.font.Font(None,40)

jumpnrunimg = pygame.image.load("./images/jumpnrun.png")
shooterimg = pygame.image.load("./images/shooter.png")
pongimg = pygame.image.load("./images/pong.png")
flappyimg = pygame.image.load("./images/flappy.png")

jumpnrun = False
shooter = False
pong = False
flappy = False

background = pygame.image.load("./images/background.png")

running = True
while running:

    if jumpnrun:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
        os.system('py "./jumpnrun.py"')
    elif shooter:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
        os.system('py "./shooter.py"')
    elif pong:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
        os.system('py "./pong.py"')
    elif flappy:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
        os.system('py "./flappy.py"')
    else:
        screen = pygame.display.set_mode((width, height), flags=pygame.SHOWN)
        screen.blit(background, (0,0))
        screen.blit(jumpnrun, (100,100))
        screen.blit(shooterimg, (100,500))
        screen.blit(pongimg, (500,100))
        screen.blit(flappyimg (500,500))

    screen.blit(copyright, (0,700))


    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()