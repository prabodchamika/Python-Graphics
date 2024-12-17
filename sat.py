import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Futuristic Alien UFO")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UFO_COLOR = (100, 150, 255)  
GLOW_COLOR = (0, 200, 255)   
LIGHT_COLOR = (255, 255, 0)  

particles = []

def add_particles(x, y):
    for _ in range(5):  
        particles.append({
            'pos': [x + random.randint(-10, 10), y + 40 + random.randint(0, 20)],
            'vel': [random.uniform(-1, 1), random.uniform(1, 3)],
            'size': random.randint(3, 6),
            'color': (0, 255, random.randint(150, 255)),
            'lifetime': 100
        })

def update_particles():
    for particle in particles[:]:
        particle['pos'][0] += particle['vel'][0]
        particle['pos'][1] += particle['vel'][1]
        particle['lifetime'] -= 1
        if particle['lifetime'] <= 0:
            particles.remove(particle)

def draw_particles():
    for particle in particles:
        pygame.draw.circle(screen, particle['color'], (int(particle['pos'][0]), int(particle['pos'][1])), particle['size'])

def generate_stars():
    return [{'pos': (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
             'speed': random.uniform(0.5, 1.5)} for _ in range(500)]

stars = generate_stars()

def update_stars():
    for star in stars:
        x, y = star['pos']
        x -= star['speed']  
        if x < 0:
            x = WIDTH
        star['pos'] = (x, y)

def draw_stars():
    for star in stars:
        x, y = star['pos']
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 1)

def draw_ufo(x, y, tilt_angle):

    tilt_x = int(15 * math.sin(tilt_angle))  
    tilt_y = int(5 * math.sin(tilt_angle))  

    pygame.draw.ellipse(screen, GLOW_COLOR, (x - 80 + tilt_x, y - 50 + tilt_y, 160, 100), 0)

    pygame.draw.ellipse(screen, UFO_COLOR, (x - 70 + tilt_x, y - 40 + tilt_y, 140, 80))

    for i in range(6):
        shade_color = (100 - i * 10, 150 - i * 15, 255 - i * 20)
        pygame.draw.ellipse(
            screen, shade_color, 
            (x - 70 + i * 3 + tilt_x, y - 40 + i * 2 + tilt_y, 140 - i * 6, 80 - i * 4), 
            2
        )

    shimmer_offset = 10 * math.sin(pygame.time.get_ticks() / 300)
    pygame.draw.ellipse(screen, (200, 200, 255), (x - 40 + tilt_x, y - 55 + tilt_y, 80, 40))  
    pygame.draw.ellipse(screen, (255, 255, 255), (x - 20 + shimmer_offset + tilt_x, y - 50 + tilt_y, 40, 20))  

    light_positions = [
        (x - 50 + tilt_x, y + 30 + tilt_y), 
        (x - 25 + tilt_x, y + 40 + tilt_y), 
        (x + tilt_x, y + 45 + tilt_y), 
        (x + 25 + tilt_x, y + 40 + tilt_y), 
        (x + 50 + tilt_x, y + 30 + tilt_y)
    ]
    for idx, pos in enumerate(light_positions):
        pulse = 5 + 4 * math.sin(pygame.time.get_ticks() / 500 + idx)  
        pygame.draw.circle(screen, LIGHT_COLOR, pos, int(pulse))
        pygame.draw.circle(screen, GLOW_COLOR, pos, int(pulse * 1.5), 1)

    add_particles(x, y)

running = True
x_ufo = WIDTH // 2  
y_ufo = HEIGHT // 2  

tilt_angle = 0  

while running:
    screen.fill(BLACK)  

    update_stars()  
    draw_stars()    

    draw_ufo(x_ufo, y_ufo, tilt_angle)  

    update_particles()  
    draw_particles()  

    tilt_angle += 0.05
    if tilt_angle > 2 * math.pi:  
        tilt_angle = 0  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
