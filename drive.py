import pygame
import time
import random

pygame.init()

d_width = 800
d_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption('Driver 2018')
clock = pygame.time.Clock()

carImg = pygame.image.load('images/car.png')

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh], 0)

def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text,largeText)
	TextRect.center = ((d_width/2),(d_height/2))
	gameDisplay.blit(TextSurf,TextRect)

	pygame.display.update()
	time.sleep(2)

	game_loop()

def crash():
	message('You Crashed')
def game_loop():
	x = (d_width * 0.45)
	y = (d_height * 0.8)

	x_change = 0

	thing_startx = random.randrange(0,d_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100

	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					pygame.quit()
					quit()
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

		gameDisplay.fill(white)

		things(thing_startx, thing_starty, thing_width, thing_height, red)
		thing_starty += thing_speed
		car(x,y)

		if x > d_width - 60 or x < 0:
			crash()

		if thing_starty > d_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, d_width)
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()


