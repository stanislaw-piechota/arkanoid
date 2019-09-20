import pygame, sys

def draw_screen(screen, settings, player, bricks):
	screen.fill(settings.screen_color)
	player.draw()
	for brick in bricks:
		brick.draw()

	pygame.display.flip()

def get_number_bricks_x(settings, brick_width):
	avaliable_space_x = settings.screen_width - 5*brick_width/4
	number_bricks_x = int(avaliable_space_x / (5*brick_width/4))
	return number_bricks_x

def create_brick(screen, settings, bricks, Brick, brick_number):
	brick = Brick(screen, settings)
	brick_width = brick.rect.width
	brick.rect.x = brick_width + 5*(brick_width * brick_number)/4
	bricks.add(brick)

def create_board(bricks, Brick, screen, settings):
	brick = Brick(screen, settings)
	number_bricks_x = get_number_bricks_x(settings,
		brick.rect.width)

	for brick_number in range(number_bricks_x):
		create_brick(screen, settings, bricks, Brick, brick_number)

def check_events(player):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				player.moving_right = True
				player.moving_left = False
			elif event.key == pygame.K_LEFT:
				player.moving_left = True
				player.moving_right = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				player.moving_right = False
			elif event.key == pygame.K_LEFT:
				player.moving_left = False

def move(player, settings):
	if player.moving_right and player.rect.x < settings.screen_width - player.width:
		player.rect.x += settings.pad_speed
	if player.moving_left and player.rect.x > 0:
		player.rect.x -= settings.pad_speed