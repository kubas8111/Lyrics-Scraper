import pygame
from constants import settings
from .Orb import Orb

class Moon(Orb):
    def __init__(self, name, position, velocity, mass, radius, father):
        super().__init__(name, position, velocity, mass, radius)
        self.father = father
            
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (settings.WIDTH_CENTER + self.position.x * settings.SCALE, settings.HEIGHT_CENTER + self.position.y * settings.SCALE), self.radius)
