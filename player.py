import pygame

class Pad:
	def __init__(self, screen, settings):
		self.settings = settings
		self.screen = screen
		self.width = 200
		self.height = 20
		self.moving_right = False
		self.moving_left = False
		self.rect = pygame.Rect((self.settings.screen_width - self.width)/2,
		 self.settings.screen_height - self.height, self.width, self.height)

	def draw(self):
		pygame.draw.rect(self.screen, self.settings.pad_color, self.rect)