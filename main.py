import pygame, sys
from pygame.sprite import Sprite, Group
from player import Pad
from settings import Settings
import game_functions as gf

class Brick(Sprite):
	def __init__(self, screen, settings):
		super(Brick, self).__init__()
		self.screen = screen
		self.settings = settings
		self.distance = 100
		self.width = 60
		self.height = 30
		self.color = (255, 0, 0)
		self.rect = pygame.Rect(self.distance, self.distance, self.width,
		 self.height)

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

pygame.init()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
player = Pad(screen, settings)
bricks = Group()

gf.create_board(bricks, Brick, screen, settings)

while True:
	gf.check_events(player)
	gf.move(player, settings)
	gf.draw_screen(screen, settings, player, bricks)