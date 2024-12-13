#Game Development
#Description: Create the classic Snake game using the pygame library.



import pygame
import time
import random

pygame.init()

# Screen settings
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 15

# Game loop
def game_loop():
    game_over = False
    snake_list = [[width // 2, height // 2]]
    food = [random.randint(0, width - snake_block), random.randint(0, height - snake_block)]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        game_display.fill(black)
        pygame.draw.rect(game_display, green, (*food, snake_block, snake_block))
        for block in snake_list:
            pygame.draw.rect(game_display, white, (*block, snake_block, snake_block))
        
        pygame.display.update()
        time.sleep(1 / snake_speed)

    pygame.quit()
    quit()

game_loop()
