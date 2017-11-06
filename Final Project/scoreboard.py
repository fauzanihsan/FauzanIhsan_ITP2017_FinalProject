import pygame.font
from pygame.sprite import Group

from player import Player

#class to report scoreboard
class Scoreboard():


    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.ai_settings = ai_settings

        #font settings for scoring
        self.text_color = (250,250,250)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_score()
        self.prep_high_score()
        self.prep_player()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        print(self.stats.score)

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.players.draw(self.screen)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        #Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_player(self):
        self.players = Group()
        for player_number in range(self.stats.ships_left):
            player = Player(self.ai_settings, self.screen)
            player.rect.x = -20
            player.rect.y = -20
            self.players.add(player)





