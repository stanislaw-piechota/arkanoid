import pygame, sys
from pygame.sprite import Sprite, Group
from player import Pad
from brick import Brick
from ball import Ball
from settings import Settings
from button import Lose
from button import Win
from scoreboard import Scoreboard
import game_functions as gf
from time import sleep

def _temp_get_fps(clock):
	if clock.get_fps():
		return clock.get_fps()
	return clock.get_fps()

pygame.init()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
player = Pad(screen, settings)
bricks = Group()
score = Scoreboard(screen, settings)
ball = Ball(screen, settings, player, bricks, score)
lose_msg = Lose(screen)
win_msg = Win(screen)

gf.create_board(bricks, Brick, screen, settings)

clock = pygame.time.Clock()
gameSpeed = 1

FPS = gameSpeed

tick = _temp_get_fps(clock)

while True:
	clock.tick(200)
	#print(tick)
	if settings.game:
		gf.check_events(player, settings)
		gf.move(player, settings, ball)
		
		gf.update_screen(screen, settings, player, bricks, ball, score)
		
		if len(bricks) == 0:
			settings.stage += 1
			win_msg.blitme()
			pygame.display.flip()
			sleep(3)
			gf.restart_game(bricks, Brick, screen, settings, ball)
			

	else:
		lose_msg.blitme()
		pygame.display.flip()
		sleep(3)
		pygame.quit()
		sys.exit()