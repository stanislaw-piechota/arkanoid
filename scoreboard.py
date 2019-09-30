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
		self.image = pygame.font.render(score_str, True, self.text_color, self.settings.screen_color)

		#dokończyć punktacje