import pygame
import random
import math
import time

pygame.init()

width, height = 450, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Symbol Decoding")

BLACK = (0, 0, 0)
GLOW_COLOR = (0, 255, 0) 
PARTICLE_COLOR = (0, 255, 128)  

font = pygame.font.SysFont("Arial", 120)

alien_symbols = ['@', '#', '%', '&', '!', '*', '?', '≈', '√', '∑', 'λ', 'ξ']

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 6)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.alpha = 255

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.alpha -= 5
        self.size -= 0.1  

    def draw(self, surface):
        pygame.draw.circle(surface, PARTICLE_COLOR, (int(self.x), int(self.y)), int(self.size))

def render_glowing_symbol(symbol, x, y, frame_count):
    glow_surface = font.render(symbol, True, GLOW_COLOR)
    glow_intensity = int(255 * (math.sin(frame_count / 20) ** 2))
    glow_surface.set_alpha(glow_intensity)
    screen.blit(glow_surface, (x - glow_surface.get_width() / 2, y - glow_surface.get_height() / 2))

def decode_animation():
    clock = pygame.time.Clock()
    running = True
    frame_count = 0
    particles = []

    while running:
        screen.fill(BLACK)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        symbol = random.choice(alien_symbols)
        x = random.randint(100, width - 100)
        y = random.randint(100, height - 100)

        render_glowing_symbol(symbol, x, y, frame_count)

        for _ in range(2):  
            particles.append(Particle(x, y))

        for particle in particles[:]:
            particle.move()
            particle.draw(screen)
            if particle.alpha <= 0: 
                particles.remove(particle)

        if frame_count % 20 == 0:
            symbol = random.choice(alien_symbols)

        frame_count += 1
        pygame.display.update()
        clock.tick(60)

decode_animation()

pygame.quit()
