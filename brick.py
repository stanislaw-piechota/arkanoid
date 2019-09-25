import pygame
from pygame.sprite import Sprite

class Brick(Sprite):
	def __init__(self, screen, settings):
		super(Brick, self).__init__()
		self.screen = screen
		self.settings = settings
		self.distance = 100
		self.width = 60
		self.height = 30
		self.color = (0, 0, 255)
		self.rect = pygame.Rect(self.distance, self.distance, self.width,
		 self.height)

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)