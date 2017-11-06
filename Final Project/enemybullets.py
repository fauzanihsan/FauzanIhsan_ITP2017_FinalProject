import pygame
from pygame.sprite import Sprite
class EnemyBullet(Sprite):
    def __init__(self, ai_settings, enemy, screen):
        super(EnemyBullet, self).__init__()
        self.screen = screen

        #initialize the bullet to rect 0,0 and set the width and height
        self.rect = pygame.Rect(0, 0, 10,1)
        self.rect.centerx = enemy.rect.centerx
        self.rect.centery = enemy.rect.centery

        self.x = float(self.rect.x)
        self.color = (0,255,0)
        self.speed = ai_settings.bullet_speed

    def update(self):
        #moving the bullet forward
        self.x -= 2


    def draw_enemybullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
