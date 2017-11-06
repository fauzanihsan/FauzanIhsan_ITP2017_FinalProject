import sys

import pygame,time

from bullet import Bullet
from pygame.sprite import *
from pygame import *
from enemy import Enemy
from time import sleep



def check_events(ai_settings,screen,stats,sb, play_button,  player,enemies,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,sb, play_button, player, enemies, bullets, mouse_x, mouse_y)


        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,player,bullets)
            if event.key == pygame.K_DOWN:
                player.moving_down = True
            elif event.key == pygame.K_UP:
                player.moving_up = True
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_RIGHT:
                player.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.moving_down = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_RIGHT:
                player.moving_right = False

#function to check the play button when the program first start
def check_play_button(ai_settings, screen, stats,sb, play_button,player, enemies,bullets, mouse_x,mouse_y):
    #to reset the game each time user click the play button
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.game_active = True
        stats.reset_stats()
        pygame.mouse.set_visible(False)
        enemies.empty()
        bullets.empty()
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_player()



        player.center_player()

def check_keydown_events(event,ai_settings,screen,player,bullets):
    if event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            pygame.mixer.pre_init(44100, -16,2,2048)
            pygame.mixer_music.load('sound/Laser Blasts-SoundBible.com-108608437.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(0)
            new_bullet = Bullet(ai_settings,screen,player)
            bullets.add(new_bullet)


def update_bullets(ai_settings, screen,stats,sb, player, enemies, bullets):
    bullets.update()
    check_bullet_enemy_collisions(ai_settings,screen, stats, sb, player,enemies,bullets)

#to check if the bullet hit the enemy ship
def check_bullet_enemy_collisions(ai_settings, screen,stats, sb, player, enemies, bullets):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    if collisions:
        stats.score += ai_settings.enemy_points
        sb.prep_score()
    check_high_score(stats, sb)


def update_enemy(ai_settings, screen, stats, sb,player, enemies, bullets):
    if pygame.sprite.spritecollideany(player, enemies):
        ship_hit(ai_settings, screen,stats, sb, player, enemies, bullets)
    check_enemies_left(ai_settings, screen,stats,sb, player, enemies, bullets)

#to reset the player's position when collision with enemies
def ship_hit(ai_settings, screen,stats, sb,player, enemies, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        enemies.empty()
        bullets.empty()
        player.center_player()
        sb.prep_player()

        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
        """Check to see if there's a new highscore"""
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()

def check_enemies_left(ai_settings, screen, stats,sb, player,enemies, bullets):
    """Check if enemies have reached the left screen"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.left <= screen_rect.left:
            ship_hit(ai_settings, screen,stats,sb, player, enemies, bullets)
            break

#function to update the screen
def update_screen(ai_settings, screen, stats, sb, player,enemies,bullets, play_button):
    ai_settings.levelup(stats.score)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #to spawn random enemies
    if pygame.time.get_ticks()%80 == 0:
        new_enemy = Enemy(ai_settings, screen)
        enemies.add(new_enemy)
    if not stats.game_active:
        play_button.draw_button()
    sb.show_score()
    player.blitme()

    if stats.game_active:
        for en in enemies:
            en.update()
            en.blitme()


    pygame.display.flip()



