import pygame

class Button:
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('images/lose.bmp')
		self.image_rect = self.image.get_rect()
		self.rect = self.image_rect
		self.rect.centerx = 600
		self.rect.centery = 325
	def blitme(self):
		self.screen.blit(self.image, self.rect)