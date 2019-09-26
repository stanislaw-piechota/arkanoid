import pygame

class Settings:
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 650
		self.screen_color = (0, 0, 0)

		self.pad_color = (255, 255, 255)
		self.pad_speed = 2

		self.number_bricks_y = 8

		self.ball_mv = False

		self.game = True