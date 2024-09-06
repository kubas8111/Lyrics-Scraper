import pygame
from objects.circle import Circle

class Circle_Statistics():
    def __init__(self, circle, color):
        self.max_x = circle.position.x
        self.min_x = self.max_x
        self.max_y = circle.position.y
        self.min_y = self.max_y
        self.p1 = circle.position.copy()
        self.p2 = circle.position.copy()
        self.p3 = circle.position.copy()
        self.p4 = circle.position.copy()
        self.radius = circle.radius
        self.color = color
        
    def update(self, circle):
        if circle.position.y >= self.max_y:
            self.p1 = circle.position.copy()
            self.max_y = circle.position.y
        if circle.position.x >= self.max_x:
            self.p2 = circle.position.copy()
            self.max_x = circle.position.x
        if circle.position.y <= self.min_y:
            self.p3 = circle.position.copy()
            self.min_y = circle.position.y
        if circle.position.x <= self.min_x:
            self.p4 = circle.position.copy()
            self.min_x = circle.position.x
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.p1.x), int(self.p1.y)), self.radius)
        pygame.draw.circle(screen, self.color, (int(self.p2.x), int(self.p2.y)), self.radius)
        pygame.draw.circle(screen, self.color, (int(self.p3.x), int(self.p3.y)), self.radius)
        pygame.draw.circle(screen, self.color, (int(self.p4.x), int(self.p4.y)), self.radius)
