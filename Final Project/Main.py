import pygame
import sys


from settings import Settings
from player import Player
from pygame.sprite import Group
from enemy import Enemy
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

import functions as gf

#the main function
def main():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    bullets = Group()
    enemies = Group()
    enemybullets = Group()
    enemy = Enemy(ai_settings, screen)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    play_button = Button(ai_settings, screen, "Play")



    pygame.display.set_caption("Space Battle")
    player = Player(ai_settings, screen)
    bground = pygame.image.load('images/wallhaven-41034.bmp')
    x = 0


    #main loop
    while True:
        gf.check_events(ai_settings, screen, stats,sb, play_button, player,enemies, bullets)

        if stats.game_active:
            player.update()
            gf.update_bullets(ai_settings, screen, stats, sb, player, enemies,bullets)
            gf.update_enemy(ai_settings, screen, stats,sb, player,enemies, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, player, enemies, bullets, play_button)

        #moving background
        screen.fill((0,0,0))
        rel_x = x % bground.get_rect().width
        screen.blit(bground, (rel_x - bground.get_rect().width,0))
        if rel_x < ai_settings.screen_width:
            screen.blit(bground, (rel_x,0))

        x -= 3


main()

#Special thanks to longlong,arkaan,and python crash course for the help of making my final project#
