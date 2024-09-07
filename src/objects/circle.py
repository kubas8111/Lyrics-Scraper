import pygame
import math
from constants import color
from constants import settings
from .entity import Entity

class Circle(Entity):
    def __init__(self, position, velocity, radius, color = color.BLACK, mass = None, name = "Ciało niebieskie"):
        super().__init__(position, velocity, mass, color)
        self.radius = radius
        self.name = name
        
        if self.mass is None:
            self.mass = self.calculate_mass()
        
    # def calculate_mass(self):
    #     return 2 * math.pi * (self.radius ** 2)
        # return (4 / 3) * math.pi * (self.radius ** 3)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (settings.WIDTH_CENTER + self.position.x * settings.SCALE, settings.HEIGHT_CENTER + self.position.y * settings.SCALE), self.radius)
