import pygame, sys
from random import randint
import math #import sin, cos

class Ball:
	def __init__(self, screen, settings, player, bricks, score):
		self.screen = screen
		self.settings = settings
		self.player = player
		self.bricks = bricks
		self.score = score
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('images/ball1.png')
		self.rect = self.image.get_rect()
		self.rect.width = 5

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.player.rect.top

		self.v = 2
		self.alfa = randint(-70,70)/180*(2*math.pi)

		self.x, self.y = self.v * math.cos(self.alfa), self.v * math.sin(self.alfa)
		print(self.x, self.y)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	"""def rand_x(self):
		x = 0
		while x == 0:
			x = randint(-3, 3)
		return x"""

	def move_ball(self):
		self.check_collision()
		if self.settings.ball_mv:
			self.rect.x += self.x
			self.rect.y += self.y

	def check_collision(self):
		if self.rect.left <= 0 or self.rect.right >= self.settings.screen_width:
			self.x *= -1
		if self.rect.top <= 0 or self.rect.colliderect(self.player.rect):
		 	self.y = -(self.y)
		if self.rect.bottom >= self.settings.screen_height:
			self.settings.game = False
		for brick in self.bricks:
			if self.rect.colliderect(brick.rect):
				self.settings.points += 100 * self.settings.stage
				self.score.prep_score()
				self.y *= -1
				self.bricks.remove(brick)
