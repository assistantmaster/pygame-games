import pygame
import random
import time
import subprocess

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

    if prozess.poll() is None:
        jumpnrun = False
        shooter = False
        pong = False
        flappy = False

    if jumpnrun:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
    elif shooter:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
    elif pong:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
    elif flappy:
        screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
    else:
        screen = pygame.display.set_mode((width, height), flags=pygame.SHOWN)
        screen.blit(background, (0,0))
        screen.blit(jumpnrunimg, (100,100))
        screen.blit(shooterimg, (100,500))
        screen.blit(pongimg, (500,100))
        screen.blit(flappyimg (500,500))
        screen.blit(copyright, (0,700))


    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos

    if 100 < mouse[0] < 300 and 100 < mouse[1] < 300:
        if keys[pygame.MOUSEBUTTONUP]:
            jumpnrun = True
            prozess = subprocess.Popen(['start', 'python', 'jumpnrun.py'], shell=True)
        screen.blit(jumpnrunimg, (90,90))
        #größenänderung bei jedem
    if 100 < mouse[0] < 300 and 500 < mouse[1] < 700:
        if keys[pygame.MOUSEBUTTONUP]:
            jumpnrun = True
            prozess = subprocess.Popen(['start', 'python', 'shooter.py'], shell=True)
        screen.blit(shooterimg, (90, 490))
        #größenänderung
    if 500 < mouse[0] < 700 and 100 < mouse[1] < 300:
        if keys[pygame.MOUSEBUTTONUP]:
            jumpnrun = True
            prozess = subprocess.Popen(['start', 'python', 'pong.py'], shell=True)
        screen.blit(pongimg, (490,90))
        #größenänderung
    if 500 < mouse[0] < 700 and 500 < mouse[1] < 700:
        if keys[pygame.MOUSEBUTTONUP]:
            jumpnrun = True
            prozess = subprocess.Popen(['start', 'python', 'flappy.py'], shell=True)
        screen.blit(flappyimg, (490,490))
        #größenänderung



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()