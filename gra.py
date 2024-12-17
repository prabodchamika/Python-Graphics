import pygame
import math
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1600, 900  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elliptical Solar System")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SUN_COLOR = (255, 255, 0)
PLANET_COLORS = {
    "Mercury": (169, 169, 169),
    "Venus": (255, 223, 0),
    "Earth": (0, 0, 255),
    "Mars": (255, 0, 0),
}

sun_pos = (WIDTH // 2, HEIGHT // 2)
planet_data = [
    {"name": "Mercury", "semi_major": 110, "semi_minor": 95, "size": 16, "orbit_speed": 0.03, "color": PLANET_COLORS["Mercury"]},
    {"name": "Venus", "semi_major": 190, "semi_minor": 170, "size": 24, "orbit_speed": 0.02, "color": PLANET_COLORS["Venus"]},
    {"name": "Earth", "semi_major": 270, "semi_minor": 240, "size": 30, "orbit_speed": 0.01, "color": PLANET_COLORS["Earth"]},
    {"name": "Mars", "semi_major": 360, "semi_minor": 330, "size": 28, "orbit_speed": 0.008, "color": PLANET_COLORS["Mars"]},
]

moon_data = {"semi_major": 50, "semi_minor": 50, "size": 8, "orbit_speed": 0.1, "color": (192, 192, 192)} 

clock = pygame.time.Clock()

def generate_stars():
    return [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(500)]

stars = generate_stars()

def update_stars():
    for i, star in enumerate(stars):
        x, y = star
        x += 1
        if x > WIDTH:
            x = 0  
        stars[i] = (x, y)

def draw_orbit_ellipse(center, semi_major, semi_minor, opacity=100):
    points = []
    for i in range(0, 360, 5): 
        x = center[0] + semi_major * math.cos(math.radians(i))
        y = center[1] + semi_minor * math.sin(math.radians(i))
        points.append((x, y))
    
    orbit_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.lines(orbit_surface, (255, 255, 255, opacity), True, points, 2)
    screen.blit(orbit_surface, (0, 0))

def draw_planet(center, planet, angle):
    planet_x = center[0] + planet["semi_major"] * math.cos(angle)
    planet_y = center[1] + planet["semi_minor"] * math.sin(angle)
    
    pygame.draw.circle(screen, planet["color"], (int(planet_x), int(planet_y)), planet["size"])

running = True
planet_angles = {planet["name"]: 0 for planet in planet_data}  
moon_angles = {planet["name"]: 0 for planet in planet_data}

while running:
    screen.fill(BLACK) 

    update_stars()
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 1)

    pygame.draw.circle(screen, SUN_COLOR, sun_pos, 50)

    for planet in planet_data:
        draw_orbit_ellipse(sun_pos, planet["semi_major"], planet["semi_minor"], opacity=60)

        draw_planet(sun_pos, planet, planet_angles[planet["name"]])

        if planet["name"] == "Earth":
            planet_x = sun_pos[0] + planet["semi_major"] * math.cos(planet_angles[planet["name"]])
            planet_y = sun_pos[1] + planet["semi_minor"] * math.sin(planet_angles[planet["name"]])

            draw_orbit_ellipse((planet_x, planet_y), moon_data["semi_major"], moon_data["semi_minor"], opacity=80)

            moon_x = planet_x + moon_data["semi_major"] * math.cos(moon_angles[planet["name"]])
            moon_y = planet_y + moon_data["semi_minor"] * math.sin(moon_angles[planet["name"]])

            pygame.draw.circle(screen, moon_data["color"], (int(moon_x), int(moon_y)), moon_data["size"])

        planet_angles[planet["name"]] += planet["orbit_speed"]
        moon_angles[planet["name"]] += moon_data["orbit_speed"]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
