import pygame
import snake as snakeClass
import apple as appleClass
import time
import random

def draw_grid():
    screen.fill(color["lightGreen"])

    flag = True
    for y in range(0, screen_size[1], cell_size):
        if flag:
            for x in range(0, screen_size[0], cell_size*2):
                pygame.draw.rect(screen, color["darkGreen"], (x, y, cell_size, cell_size))
                flag=False
        else:
            for x in range(cell_size, screen_size[0], cell_size*2):
                pygame.draw.rect(screen, color["darkGreen"], (x, y, cell_size, cell_size))
                flag=True

# Program variable
screen_size = (1200, 840)
color = {"lightGreen": "#6aa684", "darkGreen": "#4e916b", "blue": "#4a99ba", "white": "#ffffff"}
cell_size = 840//30 # defines the size cell size
AppleRegeneration = True
score = 0

# Pygame setup
pygame.init()
pygame.font.init()
pygame.display.set_caption("Snake game")
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
gameLoop = True
font = pygame.font.Font(None, 30)

# Setup snake
snake = snakeClass.Snake(cell_size, color["blue"])

# Game loop
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
            gameLoop = False
    
    # Fill the background
    draw_grid()

    # Draw the apple
    if AppleRegeneration:
        apple = appleClass.Apple(random.randint(1, (screen_size[0]//cell_size)-2)*cell_size, random.randint(1, (screen_size[1]//cell_size)-2)*cell_size, cell_size)
        AppleRegeneration = False
    apple.draw(screen)

    # Draw the snake
    keys = pygame.key.get_pressed()
    snake.direction(keys)
    snake.move()
    if snake.game_over(screen_size):
        gameLoop = False
        time.sleep(2)

    if snake.eatApple(apple):
        score += 100
        AppleRegeneration = True
        
    snake.draw(screen)

    # Display the player's score
    score_text = font.render(f"Score : {score}", True, color["white"])
    screen.blit(score_text, (20, 20))

    # Update the screen
    pygame.display.update()

    clock.tick(10) # limits FPS to 10

pygame.quit()