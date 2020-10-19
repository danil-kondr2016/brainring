#!/usr/bin/env python3

import os, pygame
import pygame.mixer, pygame.mouse
from timer import Timer

state = True

timer = Timer(60)
current_str = '0.00'

cmd = -1

score_red, score_green = 0, 0
score_plus = 1
is_red = True

pygame.mixer.init()

start_snd = pygame.mixer.Sound('timer_start.wav')
stop_snd = pygame.mixer.Sound('timer_stop.wav')
end_snd = pygame.mixer.Sound('timer_end.wav')
falstart_snd = pygame.mixer.Sound('timer_falstart.wav')

black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 255, 0)

pygame.font.init()
pygame.display.init()

score_font = pygame.font.SysFont(None, 400)
timer_font = pygame.font.SysFont('Courier New', 200)
small_font = pygame.font.SysFont('Courier New', 48)

lscreen = pygame.Surface((640, 480))
rscreen = pygame.Surface((640, 480))
screen = pygame.display.set_mode((1280, 480), pygame.FULLSCREEN)
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])
pygame.mouse.set_visible(False)

r1 = pygame.Rect(310, 230, 20, 20)

while state:
	current_str = '{:.2f}'.format(timer.current())
	if (timer.current() == timer.end) and (timer._started) and (cmd != -1):
		end_snd.play()
		cmd = -1
	lscreen.fill(black)
	if (is_red):
		pygame.draw.rect(lscreen, red, r1)
	else:
		pygame.draw.rect(lscreen, green, r1)
	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
			cmd = 0
			pygame.mixer.stop()
			start_snd.play()
			if (not timer.is_paused()):
				timer.start()
			else:
				timer.resume()
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):		
			cmd = -1
			pygame.mixer.stop()
			timer.stop()
			timer.null()
		if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 3) and (cmd not in {1, 2}):
			if (timer.is_started()):
				cmd = 1
				timer.pause()
				pygame.mixer.stop()
				stop_snd.play()
			else:
				cmd = 3
				pygame.mixer.stop()
				falstart_snd.play()
				break
		if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 2) and (cmd not in {1, 2}):
			if (timer.is_started()):
				cmd = 2
				timer.pause()
				pygame.mixer.stop()
				stop_snd.play()
			else:
				cmd = 4
				pygame.mixer.stop()
				falstart_snd.play()
				break
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
			pygame.mixer.quit()
			pygame.display.quit()
			pygame.font.quit()
			state = False
			break
	if (cmd == 1):
		rscreen.fill(red)
	elif (cmd == 2):
		rscreen.fill(green)
	else:
		rscreen.fill(black)
	if (cmd == 3):
		zeit = timer_font.render(current_str, True, red)
	elif (cmd == 4):
		zeit = timer_font.render(current_str, True, green)
	else:
		zeit = timer_font.render(current_str, True, white)
	red_score = score_font.render(("%d" % score_red), True, red)
	green_score = score_font.render(("%d" % score_green), True, green)
	plus_score = small_font.render(("%d" % score_plus), True, white)
	lscreen.blit(red_score, [(lscreen.get_width()//2 - red_score.get_width()) // 2, (lscreen.get_height() - red_score.get_height()) // 2])
	lscreen.blit(green_score, [((lscreen.get_width()//2 - green_score.get_width()) // 2)+lscreen.get_width()//2, (lscreen.get_height() - green_score.get_height()) // 2])
	lscreen.blit(plus_score, [(lscreen.get_width()-plus_score.get_width())//2, 436])
	rscreen.blit(zeit, [(rscreen.get_width()-zeit.get_width())//2, (rscreen.get_height()-zeit.get_height())//2])
	screen.blit(lscreen, [0, 0])
	screen.blit(rscreen, [(screen.get_width())//2, 0])
	pygame.display.update()
