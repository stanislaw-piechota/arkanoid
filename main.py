import pygame, sys
from pygame.sprite import Sprite, Group
from player import Pad
from brick import Brick
from ball import Ball
from settings import Settings
from button import Button
import game_functions as gf
from time import sleep

pygame.init()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
player = Pad(screen, settings)
bricks = Group()
ball = Ball(screen, settings, player, bricks)
lose_msg = Button(screen)

gf.create_board(bricks, Brick, screen, settings)

clock = pygame.time.Clock()

while True:
	tick = 293 - len(bricks) - ball.x
	clock.tick(tick)
	if settings.game:
		gf.check_events(player, settings)
		gf.move(player, settings, ball)
		gf.update_screen(screen, settings, player, bricks, ball)
	else:
		lose_msg.blitme()
		pygame.display.flip()
		sleep(3)
		sys.exit()
