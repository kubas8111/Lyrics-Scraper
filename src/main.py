import pygame
import math
from setup import orbs
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
        for orb in orbs:
            total_force = pygame.Vector2(0, 0) # zero force at begining
            
            for other_orb in orbs:
                if orb != other_orb:
                    force = orb.gravitational_force(other_orb)
                    total_force += force
                    
            # All forces for one orb
            orb.apply_force(total_force)
        
        for orb in orbs:
            orb.update(settings.FIXED_DT)
            orb.draw(screen)
            
        # orb_stats.update(orbs[1])
        # orb_stats.draw(screen)
        
        accumulated_time -= settings.FIXED_DT
    
    
    
    # --- Statistics ---
    y_offset = 10
    for i, orb in enumerate(orbs):
        mass_text = font.render(f"{orb.name} - Masa: {orb.mass:.5e}kg", True, color.WHITE)
        position_text = font.render(f"{orb.name} - Pozycja: ({orb.position.x:.1f}, {orb.position.y:.1f})", True, color.WHITE)
        velocity_text = font.render(f"{orb.name} - Prędkość: ({orb.velocity.x:.1f}, {orb.velocity.y:.1f})", True, color.WHITE)
        
        # Display of mass, position and velocity, and then more space for another orb
        screen.blit(mass_text, (10, y_offset))
        y_offset += settings.FONT_SIZE + 5
        screen.blit(position_text, (10, y_offset))
        y_offset += settings.FONT_SIZE + 5
        screen.blit(velocity_text, (10, y_offset))
        y_offset += settings.FONT_SIZE + 10
    
    # min_max_text = font.render(f"Max_x: {orb_stats.max_x:.1f} Max_y: {orb_stats.max_y:.1f}", True, color.WHITE)
    # min_max_text3 = font.render(f"Min_x: {orb_stats.min_x:.1f} Min_y: {orb_stats.min_y:.1f}", True, color.WHITE)
    
    # screen.blit(min_max_text, (10, y_offset))
    # y_offset += settings.FONT_SIZE + 5
    # screen.blit(min_max_text3, (10, y_offset))
    # y_offset += settings.FONT_SIZE + 5
    
    pygame.display.flip()
    
pygame.quit()
