import pygame
from pygame.draw import *
from constant import *
import json

pygame.init()
font = pygame.font.SysFont('serif', paragraph)
fontHead = pygame.font.SysFont('serif', 2*paragraph)
Clock = pygame.time.Clock()
Win = pygame.display.set_mode((winX,winY))
def init():
	pygame.init()
	pygame.display.set_caption("GAME THE BALLS")
	pygame.mixer.music.load("resource/sound.oga")
	pygame.mixer.music.play()
	dataUp()
	pygame.display.update()


def dataUp():
	global Data
	with open("resource/data.json", "r") as read_file: 
		Data = json.load(read_file)
def dataDown():
	global Data
	with open("resource/data.json","w") as write_file:
		json.dump(Data,write_file) 
 