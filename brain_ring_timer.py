#!/usr/bin/env python3

import sys, pygame
import pygame.mixer, pygame.mouse
from timer import Timer

state = True

timer = Timer(60)
current_str = '0.00'

cmd = -1

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

rscreen = pygame.Surface((640, 480))
screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])
pygame.mouse.set_visible(False)

r1 = pygame.Rect(310, 230, 20, 20)

while state:
	current_str = '{:.2f}'.format(timer.current())
	if (timer.current() == timer.end) and (timer._started) and (cmd != -1):
		end_snd.play()
		cmd = -1
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
	rscreen.blit(zeit, [(rscreen.get_width()-zeit.get_width())//2, (rscreen.get_height()-zeit.get_height())//2])
	screen.blit(rscreen, [0, 0])
	pygame.display.update()
