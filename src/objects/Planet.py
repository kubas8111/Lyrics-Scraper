import pygame
from constants import settings
from .Orb import Orb
from .Star import Star

class Planet(Orb):
    def __init__(self, name, position, velocity, mass, radius, father = None, moons = None):
        super().__init__(name, position, velocity, mass, radius)
        if isinstance(father, Star):
            self.father = father
            self.father.add_planets(self)
        if moons:
            self.moons = [moon for moon in moons]
        else:
            self.moons = []
    
    def add_moons(self, moons):
        self.moons.extend(moons)
            
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (settings.WIDTH_CENTER + self.position.x * settings.SCALE, settings.HEIGHT_CENTER + self.position.y * settings.SCALE), self.radius)

    def set_father(self, father):
        self.father = father
