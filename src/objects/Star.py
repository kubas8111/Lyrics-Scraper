import pygame
from constants import settings
from .Orb import Orb

class Star(Orb):
    def __init__(self, name, position, velocity, mass, radius, planets = None):
        super().__init__(name, position, velocity, mass, radius)
        self.planets = []
        self.add_planets(planets)
    
    def add_planets(self, planets):
        if planets:
            if not isinstance(planets, list):
                planets = [planets]
            
            for planet in planets:
                if planet in self.planets:
                    continue
                
                self.planets.append(planet)
                planet.set_father(self)
                print(f"dodano planetę {planet.name}")
            
    def apply_father_velocity(self):
        pass
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (settings.WIDTH_CENTER + self.position.x * settings.SCALE, settings.HEIGHT_CENTER + self.position.y * settings.SCALE), self.radius)
