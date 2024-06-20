import pygame

class Snake:
    def __init__(self, cell_size, color):
        self.cell_size = cell_size
        self.color = color
        self.x_pos = cell_size*15
        self.y_pos = cell_size*15
        self.x_direction = 0
        self.y_direction = 1
        self.snake_size = 1
        self.snake = [pygame.Rect(self.x_pos, self.y_pos, self.cell_size, self.cell_size)]


    def direction(self, keys):
        if keys[pygame.K_UP]:
            if self.x_direction==1 or self.x_direction==-1: # Prevent the player from going back
                self.y_direction = -1
                self.x_direction = 0
        elif keys[pygame.K_DOWN]:
            if self.x_direction==1 or self.x_direction==-1:
                self.y_direction = 1
                self.x_direction = 0
        elif keys[pygame.K_LEFT]:
            if self.y_direction==1 or self.y_direction==-1:
                self.y_direction = 0
                self.x_direction = -1
        elif keys[pygame.K_RIGHT]:
            if self.y_direction==1 or self.y_direction==-1:
                self.y_direction = 0
                self.x_direction = 1

    def move(self):
        # Change the player's position
        self.x_pos += self.x_direction*self.cell_size
        self.y_pos += self.y_direction*self.cell_size

        # Update the snake positon
        self.snake.append(pygame.Rect(self.x_pos, self.y_pos, self.cell_size, self.cell_size))

        del self.snake[0]

    def game_over(self, screen_size):
        # Return false when the player is outside the game
        if self.x_pos<0 or self.x_pos>screen_size[0]-self.cell_size:
            return True
        if self.y_pos<0 or self.y_pos>screen_size[1]-self.cell_size:
            return True
        
        # Check if the snake's head collides with its own body
        head_rect = self.snake[-1]
        for segment in self.snake[:-1]:
            if head_rect.colliderect(segment):
                return True

    def eatApple(self, apple):
        if self.snake[0].colliderect(apple.rect):
            self.snake_size += 1
            self.snake.append(pygame.Rect(self.x_pos, self.y_pos, self.cell_size, self.cell_size))
            self.grow = True
            return True

    def draw(self, screen):
        # Draw the snake
        for rect in self.snake:
            pygame.draw.rect(screen, self.color, rect)