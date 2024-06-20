import pygame

class Apple:
    def __init__(self, x_pos, y_pos, cell_size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.cell_size = cell_size
        self.color = "#ed3755"
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.cell_size, self.cell_size)
    
    def draw(self, screen):
        # Draw the apple
        pygame.draw.rect(screen, self.color, self.rect)