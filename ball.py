import pygame

class Ball:
	def __init__(self, screen, settings, player):
		self.screen = screen
		self.settings = settings
		self.player = player
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('images/ball1.png')
		self.rect = self.image.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = player.rect.top

		self.x, self.y = self.rand_x(), 1

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def rand_x(self):
		from random import randint
		x = 0
		while x == 0:
			x = randint(-1, 1)
		return x

	def move_ball(self):
		self.check_collision()
		if self.settings.ball_mv:
			self.rect.x += self.x
			self.rect.y += self.y

	def check_collision(self):
		if self.rect.left <= 0 or self.rect.right >= self.settings.screen_width:
			self.x *= -1
		if self.rect.top <= 0 or self.rect.bottom >= self.settings.screen_height or self.rect.colliderect(self.player.rect):
		 	self.y = -(self.y)
		 #if self.rect.collidepoint
		 # dokończyć kolizję z blokami