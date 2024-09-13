import pygame
import math
from objects import *
import constants.settings as settings
import constants.color as color
import constants.physics as ph

planets = [
    # SUN
    Circle(pygame.Vector2(0, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 1.5, color.YELLOW, 1.9891e30, "Sun"),
    # PLANETS
    Circle(pygame.Vector2(0 + 5.79e7, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 0.3825, color.BROWN, 3.302e23, "Mercury"),
    Circle(pygame.Vector2(0 + 1.08e8, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 0.9489, color.ORANGE, 4.8685e24, "Venus"),
    Circle(pygame.Vector2(0 + 1.496e8, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE, color.BLUE, 5.9742e24, "Earth"),
    Circle(pygame.Vector2(0 + 2.279e8, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 0.5335, color.RED, 6.419e23, "Mars"),
    Circle(pygame.Vector2(0 + 7.784e8, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 11.2092, color.GOLD, 1.8986e27, "Jupiter"),
    Circle(pygame.Vector2(0 + 1.4267e9, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 9.4494, color.OLIVE, 5.685e26, "Saturn"),
    Circle(pygame.Vector2(0 + 2.871e9, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 4.0074, color.LIGHT_GRAY, 8.6841e25, "Uranus"),
    Circle(pygame.Vector2(0 + 4.498e9, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 3.8827, color.CYAN, 1.0244e26, "Neptun"),
    # MOON
    Circle(pygame.Vector2(0 + 1.496e8 + 3.8e5, 0), pygame.Vector2(0, 0), ph.EARTH_RADIUS * settings.PLANET_SCALE * 0.2731, color.GRAY, 7.34877e22, "Moon"),
]


# added multiply by 60
for planet in planets[1:]:
    planet.apply_velocity(pygame.Vector2(0, math.sqrt(ph.G * planets[0].mass / planet.distance_to(planets[0]) * 60)))
    print(math.sqrt(ph.G * planets[0].mass / planet.distance_to(planets[0])))
    
planets[-1].apply_velocity(pygame.Vector2(0, math.sqrt(ph.G * planets[3].mass / planet.distance_to(planets[3]) * 60)))