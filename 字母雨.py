import random
import pygame

WIDTH = 2048
HEIGHT = 1200

FONT_WIDTH = 15
pygame.init()
winSur = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("font.ttf", 25)
bg_suface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)

pygame.Surface.convert(bg_suface)

bg_suface.fill(pygame.Color(0, 0, 0, 28))
winSur.fill((0, 0, 0))
letter = ['C', 'H', 'A', 'N', 'G', 'H', 'A', 'O', 'N', 'B']
texts = [font.render(str(letter[i]),
                     True,
                     (random.randint(0, 255),
                      random.randint(0, 225),
                      random.randint(0, 225))) for i in range(10)]
column = int(WIDTH / FONT_WIDTH)

drops = [0 for i in range(column)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(30)
    winSur.blit(bg_suface, (0, 0))

    for i in range(len(drops)):
        text = random.choice(texts)
        winSur.blit(text, (i * FONT_WIDTH, drops[i] * FONT_WIDTH))

        drops[i] += 1

        if drops[i] * 10 > HEIGHT or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip()
