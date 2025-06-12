import pygame
import random
import time

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reaktionsklicker")
pygame.display.set_icon(pygame.image.load("./images/favicon5.png"))

font = pygame.font.Font(None,20)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None,40)

text = font3.render("", True, (255,255,255))
background = pygame.image.load("./images/background5.png")
copyright = font.render('© 2025 by assistantmaster', True, (150,150,150))

x = int(random.randint(0,width - 64))
y = int(random.randint(0,height - 64))
zeit = 0
highscore = float('inf')
mouse = False

clock = pygame.time.Clock()
running = True
while running:
    if highscore != float('inf'):
        pygame.display.set_caption(f"Reaktionsklicker - Dein Highscore: {highscore/100:.2f} Sekunden")
    text_rect = text.get_rect(center=(width//2, height//2))
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255,0,0), (x, y, 64, 64))
    screen.blit(text, text_rect)
    screen.blit(copyright, (0,700))

    zeit += 1

    if mouse:
        if x <= mouse_pos[0] <= x + 64 and y <= mouse_pos[1] <= y + 64 :
            x = int(random.randint(0,width - 64))
            y = int(random.randint(0,height - 64))
            text = font3.render(f"Deine Reaktionszeit: {zeit/100:.2f} Sekunden", True, (255,255,255))
            if zeit < highscore:
                highscore = zeit
            zeit = 0
            pygame.mixer.music.load("./sounds/punkt.mp3")
            pygame.mixer.music.play(1)

        else:
            running = False
            pygame.mixer.music.load("./sounds/verloren.mp3")
            pygame.mixer.music.play(1)
            pygame.display.set_caption("Reaktionsklicker")
            screen.fill((255, 0, 0))
            text = font3.render("Verloren", True, (255,255,255))
            highscoretext = font3.render(f"Dein Highscore war {highscore/100:.2f} Sekunden", True, (255,255,255))
            text_rect = text.get_rect(center=(width//2, height//2))
            highscoretext_rect = highscoretext.get_rect(center=(width//2, height//2+100))
            screen.blit(text, text_rect)
            screen.blit(highscoretext, highscoretext_rect)
            pygame.display.flip()
            pygame.time.delay(3000)

        mouse = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            mouse = True
            

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
