import pygame
from .entity import Entity

class Square(Entity):
    def __init__(self, x, y, m, size, color):
        super().__init__(x, y, m, color)
        self.size = size
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
