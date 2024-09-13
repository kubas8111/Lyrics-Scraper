import pygame
import math
from setup import planets
from objects import *
import constants.settings as settings
import constants.color as color
import constants.physics as ph

# game settings
pygame.init()
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()

# font settings
font = pygame.font.SysFont("Arial", settings.FONT_SIZE)

dt = 1 / settings.FPS
accumulated_time = 0    # buffer needed for speeding up the simulation


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(color.BLACK)
    
    
    dt = clock.tick(settings.FPS) / 1000
    accumulated_time += dt * ph.SIM_SPEED

    # Updating physics in it's real time
    while accumulated_time >= settings.FIXED_DT:
        # --- ALL PHYSICS HERE ---
        for planet in planets:
            total_force = pygame.Vector2(0, 0) # zero force at begining
            
            for other_planet in planets:
                if planet != other_planet:
                    force = planet.gravitational_force(other_planet)
                    total_force += force
                    
            # All forces for one planet
            planet.apply_force(total_force)
        
        for planet in planets:
            planet.update(settings.FIXED_DT)
            planet.draw(screen)
            
        # planet_stats.update(planets[1])
        # planet_stats.draw(screen)
        
        accumulated_time -= settings.FIXED_DT
    
    
    
    # --- Statistics ---
    y_offset = 10
    for i, planet in enumerate(planets):
        mass_text = font.render(f"{planet.name} - Masa: {planet.mass:.5e}kg", True, color.WHITE)
        position_text = font.render(f"{planet.name} - Pozycja: ({planet.position.x:.1f}, {planet.position.y:.1f})", True, color.WHITE)
        velocity_text = font.render(f"{planet.name} - Prędkość: ({planet.velocity.x:.1f}, {planet.velocity.y:.1f})", True, color.WHITE)
        
        # Display of mass, position and velocity, and then more space for another planet
        screen.blit(mass_text, (10, y_offset))
        y_offset += settings.FONT_SIZE + 5
        screen.blit(position_text, (10, y_offset))
        y_offset += settings.FONT_SIZE + 5
        screen.blit(velocity_text, (10, y_offset))
        y_offset += settings.FONT_SIZE + 10
    
    # min_max_text = font.render(f"Max_x: {planet_stats.max_x:.1f} Max_y: {planet_stats.max_y:.1f}", True, color.WHITE)
    # min_max_text3 = font.render(f"Min_x: {planet_stats.min_x:.1f} Min_y: {planet_stats.min_y:.1f}", True, color.WHITE)
    
    # screen.blit(min_max_text, (10, y_offset))
    # y_offset += settings.FONT_SIZE + 5
    # screen.blit(min_max_text3, (10, y_offset))
    # y_offset += settings.FONT_SIZE + 5
    
    pygame.display.flip()
    
pygame.quit()
