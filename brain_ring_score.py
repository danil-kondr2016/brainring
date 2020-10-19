#!/usr/bin/env python3

import sys, pygame
import pygame.mouse

state = True

score_red, score_green = 0, 0
score_plus = 1
is_red = True

black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 255, 0)

pygame.font.init()
pygame.display.init()

score_font = pygame.font.SysFont(None, 400)
small_font = pygame.font.SysFont('Courier New', 48)

lscreen = pygame.Surface((640, 480))
screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])
pygame.mouse.set_visible(False)

r1 = pygame.Rect(310, 230, 20, 20)

while state:
	lscreen.fill(black)
	if (is_red):
		pygame.draw.rect(lscreen, red, r1)
	else:
		pygame.draw.rect(lscreen, green, r1)
	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_KP_DIVIDE):
			is_red = not is_red
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_KP_PLUS) and (is_red):
			score_red += score_plus
			score_plus = 1
		elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_KP_PLUS) and not (is_red):
			score_green += score_plus
			score_plus = 1
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT):
			score_plus -= 1
			if (score_plus <= 0):
				score_plus = 1
		elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RIGHT):
			score_plus += 1
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_BACKSPACE):
			score_red = 0
			score_green = 0
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
			pygame.display.quit()
			pygame.font.quit()
			state = False
			break
	red_score = score_font.render(("%d" % score_red), True, red)
	green_score = score_font.render(("%d" % score_green), True, green)
	plus_score = small_font.render(("%d" % score_plus), True, white)
	lscreen.blit(red_score, [(lscreen.get_width()//2 - red_score.get_width()) // 2, (lscreen.get_height() - red_score.get_height()) // 2])
	lscreen.blit(green_score, [((lscreen.get_width()//2 - green_score.get_width()) // 2)+lscreen.get_width()//2, (lscreen.get_height() - green_score.get_height()) // 2])
	lscreen.blit(plus_score, [(lscreen.get_width()-plus_score.get_width())//2, 436])
	screen.blit(lscreen, [0, 0])
	pygame.display.update()
