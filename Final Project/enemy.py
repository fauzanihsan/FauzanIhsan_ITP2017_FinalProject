import pygame
import random
from pygame.sprite import Sprite

class Enemy(Sprite):
    """a class to represent a single enemy"""
    def __init__(self, ai_settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        self.image = pygame.image.load('images/cartoon-spaceship1.png')
        self.rect = self.image.get_rect()
        self.rect.right = 1300


        self.rect.y = random.randint(0,500)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)





    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.right -= self.ai_settings.enemy_speed_factor + self.ai_settings.level







