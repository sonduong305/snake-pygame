import pygame
from config import config
import numpy as np
import random


class food(object):
    
    def __init__(self, x, y):
        self.cor = [x, y]
        
    def draw(self, win):
        kt = 25
        pygame.draw.rect(win, (255,0,0), (self.cor[0] * kt, self.cor[1] * kt, kt, kt))

    def generate(self):
        self.cor = [random.randint(0,39), random.randint(0,39)] 