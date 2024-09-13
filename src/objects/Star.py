import pygame
from constants import settings
from .Orb import Orb

class Star(Orb):
    def __init__(self, name, position, velocity, mass, radius, planets = None):
        super().__init__(name, position, velocity, mass, radius)
        if planets:
            self.planets = [planet for planet in planets]
        else:
            self.planets = []
    
    def add_planets(self, planets):
        self.planets.extend(planets)
            
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (settings.WIDTH_CENTER + self.position.x * settings.SCALE, settings.HEIGHT_CENTER + self.position.y * settings.SCALE), self.radius)
