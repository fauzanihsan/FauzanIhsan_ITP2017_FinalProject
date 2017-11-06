import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, player):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery

        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color


    def update(self):
        self.x += 10
        self.rect.x = self.x


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



