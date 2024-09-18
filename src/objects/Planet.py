import pygame
import math
from constants import physics as ph
from constants import settings
from .Orb import Orb
from .Star import Star

class Planet(Orb):
    def __init__(self, name, position, velocity, mass, radius, father = None, moons = None):
        super().__init__(name, position, velocity, mass, radius)
        self.father = None
        self.moons = []
        if isinstance(father, Star):
            self.father = father
            self.father.add_planets(self)
        self.add_moons(moons)
    
    def add_moons(self, moons):
        if moons:
            if not isinstance(moons, list):
                moons = [moons]
            
            for moon in moons:
                if moon in self.moons:
                    continue
                
                self.moons.append(moon)
                moon.set_father(self)
                print(f"dodano księżyc {moon.name}")
            
    def apply_father_velocity(self):
        self.apply_velocity(pygame.Vector2(0, math.sqrt(ph.G * self.father.mass / self.distance_to(self.father) * 60)))
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (settings.WIDTH_CENTER + self.position.x * settings.SCALE, settings.HEIGHT_CENTER + self.position.y * settings.SCALE), self.radius)

    def set_father(self, father):
        self.father = father
        print(self.father.name)
