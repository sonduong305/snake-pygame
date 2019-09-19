import pygame
from player import player
from config import config
from food import food
pygame.init()

win_size = config.size
win = pygame.display.set_mode(win_size)
pygame.display.set_caption("First Game")
run = True
clock = pygame.time.Clock()
man = player(12, 12)
food = food(3, 3)
food.generate()
def redrawGameWindow():
    pygame.draw.rect(win, (0, 0, 0), (0, 0, win_size[0], win_size[1]))
    food.draw(win)
    man.draw(win)
    
    pygame.display.update()


while run:
    clock.tick(16)
    keys = pygame.key.get_pressed()

    if man.snake[0] == food.cor:
        while(food.cor == man.snake[0]):
            food.generate()
        man.snake.append(man.snake[len(man.snake) - 1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if keys[pygame.K_LEFT]:
        if(man.heading != "right"):
            man.heading = "left"

    elif keys[pygame.K_RIGHT]:
        if(man.heading != "left"):
            man.heading = "right"

    elif keys[pygame.K_UP]:
        if(man.heading != "down"):
            man.heading = "up"
        
    elif keys[pygame.K_DOWN]:
        if(man.heading != "up"):
            man.heading = "down"
    man.move()
    if man.chet():
        pygame.quit()
    redrawGameWindow()
pygame.quit()