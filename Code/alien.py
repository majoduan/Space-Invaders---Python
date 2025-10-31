import pygame
from pathlib import Path


class Alien(pygame.sprite.Sprite):
    def __init__(self, enemies, x, y):
        super().__init__()
        BASE_DIR = Path(__file__).resolve().parent.parent
        GRAPHICS_DIR = BASE_DIR / 'Graphics'
        self.image = pygame.image.load(str(GRAPHICS_DIR / f"{enemies}.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))


        #Puntuacion de Aliens
        if enemies == 'yellow':
            self.score_value = 15  # Puntuación para alienígenas amarillos
        elif enemies == 'green':
            self.score_value = 10  # Puntuación para alienígenas verdes
        elif enemies == 'red':
            self.score_value = 5  # Puntuación para alienígenas rojos
        elif enemies == 'extra':
            self.score_value = 20  # Puntuación para otros alienígenas

    def update(self, direction):
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        BASE_DIR = Path(__file__).resolve().parent.parent
        GRAPHICS_DIR = BASE_DIR / 'Graphics'
        self.image = pygame.image.load(str(GRAPHICS_DIR / 'extra.png')).convert_alpha()

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft = (x, 80))

    def update(self):
        self.rect.x += self.speed