import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self,ai_settings, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/futuramaship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.center = float(self.rect.centery)


        self.moving_down = False
        self.moving_up = False
        self. moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_down and self.center <= self.screen_rect.bottom:
            self.center += self.ai_settings.player_speed_factor

        if self.moving_up and self.center >= self.screen_rect.top:
            self.center -= self.ai_settings.player_speed_factor

        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.left += self.ai_settings.player_speed_factor

        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.rect.left -= self.ai_settings.player_speed_factor

        self.rect.centery = self.center



    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_player(self):
        self.center = self.screen_rect.centery
        self.rect.left = self.screen_rect.left



