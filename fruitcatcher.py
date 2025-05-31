import pygame
import random
import time

pygame.init()

width = 1280 
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fruit Catcher")
pygame.display.set_icon(pygame.image.load("./images/favicon6.png"))

font = pygame.font.Font(None,20)
font2 = pygame.font.Font(None,100)
font3 = pygame.font.Font(None,40)

background = pygame.image.load("./images/background6.jpg")
player = pygame.image.load("./images/player6.png")
copyright = font.render('© 2025 by assistantmaster', True, (150,150,150))

fruitimgs = [
    pygame.image.load("./images/apple.png")
]

playerx = 600
fruitspeed = 5
fruitfrequency = 40
fruitindex = fruitfrequency
punkte = 0
gamelength = 60

def new_fruit():
    fruitimg = random.choice(fruitimgs)
    fruitx = random.randint(0, width - fruitimg.get_width())
    fruity = -fruitimg.get_height()
    return {"image": fruitimg, "x": fruitx, "y": fruity}

fruits = []

starttime = time.time()

clock = pygame.time.Clock()
running = True
while running:

    currenttime = int(time.time() - starttime)
    timeleft = gamelength-currenttime
    timeleftmin = int(timeleft//60)
    timeleftsec = int(timeleft%60)
    if timeleftsec < 10:
        timeleftsec = f"0{timeleftsec}"

    punktedisplay = font3.render(f'Punkte: {punkte}', True, (255,255,255))
    timedisplay = font3.render(f'{timeleftmin}:{timeleftsec}', True, (255,255,255))

    screen.blit(background, (0,0))
    screen.blit(player, (playerx, 600))
    screen.blit(punktedisplay, (20,20))
    screen.blit(timedisplay, (screen.get_width() // 2 - timedisplay.get_width() // 2, 20))
    screen.blit(copyright, (0,700))

    for fruit in fruits[:]:
        fruit["y"] += fruitspeed
        screen.blit(fruit["image"], (fruit["x"], fruit["y"]))
        fruit_rect = pygame.Rect(fruit["x"], fruit["y"], fruit["image"].get_width(), fruit["image"].get_height())
        player_rect = pygame.Rect(playerx, 600, player.get_width(), player.get_height())

        if player_rect.colliderect(fruit_rect):
            punkte += 1
            pygame.mixer.music.load("./sounds/punkt.mp3")
            pygame.mixer.music.play(1)
            fruits.remove(fruit)
        elif fruit["y"] > height:
            fruits.remove(fruit)
            punkte -= 1

    if fruitindex >= fruitfrequency:
        fruits.append(new_fruit())
        fruitindex = 0

    fruitindex += 1


    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    playerx = mouse[0] - 75


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if int(timeleft) == 0:
        screen.blit(background, (0,0))
        screen.blit(player, (playerx, 600))
        screen.blit(punktedisplay, (20,20))
        screen.blit(timedisplay, (screen.get_width() // 2 - timedisplay.get_width() // 2, 20))
        screen.blit(copyright, (0,700))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()