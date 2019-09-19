import pygame
from config import config
import numpy as np

class player(object):
    
    def __init__(self, x, y):
        self.snake = [[x, y] , [x , y + 1], [x , y + 2]]
        self.heading = "right"
        
    
    def move(self):
        if(self.heading == "left"):
            self.snake.insert(0, [self.snake[0][0] - 1, self.snake[0][1]])
            self.snake.pop(len(self.snake) - 1)
        elif (self.heading == "right"):
            self.snake.insert(0, [self.snake[0][0] + 1, self.snake[0][1]])
            self.snake.pop(len(self.snake) - 1)
        elif (self.heading == "up"):
            self.snake.insert(0, [self.snake[0][0], self.snake[0][1] - 1])
            self.snake.pop(len(self.snake) - 1)
        elif (self.heading == "down"):
            self.snake.insert(0, [self.snake[0][0], self.snake[0][1] + 1])
            self.snake.pop(len(self.snake) - 1)
        self.tong_tuong()
        
        # self.hitbox = (self.x - 25, self.y - 25, 25*3, 25*3)

    def draw(self, win):
        kt = 25
        for cor in self.snake:
            pygame.draw.rect(win, (255,255,255), (cor[0] * kt, cor[1] * kt, kt, kt))
    def tong_tuong(self):
        if self.snake[0][0] == -1:
            self.snake[0][0] = 39
        if self.snake[0][0] == 40:
            self.snake[0][0] = 0
        if self.snake[0][1] == -1:
            self.snake[0][1] = 39
        if self.snake[0][1] == 40:
            self.snake[0][1] = 0

    def chet(self):
        if (self.snake[0] in self.snake[1:]):
            return True
        return False