import pygame
from constants import physics as ps
from constants import color

class Orb:
    def __init__(self, name, position, velocity, mass, radius):
        self.name = name
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.mass = mass
        self.radius = radius
        self.color = color.RED
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def apply_force(self, force):
        if self.mass != 0:
            acceleration = force / self.mass
            self.velocity += acceleration
            
    def apply_velocity(self, velocity):
        self.velocity += velocity
        
    def gravitational_force(self, other):
        r = self.distance_to(other)
        if r == 0:
            return pygame.Vector2(0,0)
        
        force = ps.G * (self.mass * other.mass) / (r ** 2)
        direction = (other.position - self.position).normalize()
        
        return direction * force
    
    def distance_to(self, other):
        return self.position.distance_to(other.position)
    
    # --- Setters ---
    
    def set_position(self, position):
        self.position = pygame.Vector2(position)
    
    def set_velocity(self, velocity):
        self.velocity = pygame.Vector2(velocity)
    
    def set_mass(self, mass):
        if mass > 0:
            self.mass = mass
        else:
            raise ValueError("Mass must be greater than 0")