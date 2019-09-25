import pygame, sys
from pygame.sprite import Sprite, Group
from player import Pad
from brick import Brick
from ball import Ball
from settings import Settings
import game_functions as gf

pygame.init()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
player = Pad(screen, settings)
bricks = Group()
ball = Ball(screen, settings, player)

print(ball.rect.left)

gf.create_board(bricks, Brick, screen, settings)

while True:
	gf.check_events(player, settings)
	gf.move(player, settings, ball)
	gf.update_screen(screen, settings, player, bricks, ball)