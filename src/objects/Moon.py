import pygame
import math
from constants import physics as ph
from constants import settings
from .Orb import Orb

class Moon(Orb):
    def __init__(self, name, position, velocity, mass, radius, father = None):
        super().__init__(name, position, velocity, mass, radius)
        self.father = father
        
    def apply_father_velocity(self):
        self.apply_velocity(pygame.Vector2(0, math.sqrt(ph.G * self.father.mass / self.distance_to(self.father) * 60)) + self.father.velocity)
            
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (settings.WIDTH_CENTER + self.position.x * settings.SCALE, settings.HEIGHT_CENTER + self.position.y * settings.SCALE), self.radius)

    def set_father(self, father):
        self.father = father
        print(self.father.name)
