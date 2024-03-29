import pygame.font

class Scoreboard:
	def __init__(self, screen, settings):
		self.screen = screen
		self.settings = settings
		self.screen_rect = screen.get_rect()

		self.text_color = (220, 220, 220)
		self.font = pygame.font.SysFont(None, 36)

		self.prep_score()

	def prep_score(self):
		score_str = str(self.settings.points)
		self.image = self.font.render(score_str, True, self.text_color, self.settings.screen_color)

		self.rect = self.image.get_rect()
		self.rect.right = 60
		self.rect.bottom = 630

	def show_score(self):
		self.screen.blit(self.image, self.rect)