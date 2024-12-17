import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Rain")

BLACK = (0, 0, 0)
NEON_COLORS = [(0, 255, 255) ]

NUM_DROPS = 100
DROPS = []

for _ in range(NUM_DROPS):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, 0)
    speed = random.uniform(2, 5)
    color = random.choice(NEON_COLORS)
    length = random.randint(10, 20)
    DROPS.append({"x": x, "y": y, "speed": speed, "color": color, "length": length})

def draw_glow(surface, color, position, radius):
    glow = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    for i in range(radius, 0, -1):
        alpha = int(255 * (1 - i / radius))
        pygame.draw.circle(glow, (*color, alpha), (radius, radius), i)
    surface.blit(glow, (position[0] - radius, position[1] - radius))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for drop in DROPS:
        drop["y"] += drop["speed"]  
        if drop["y"] > HEIGHT:     
            drop["y"] = random.randint(-HEIGHT, 0)
            drop["x"] = random.randint(0, WIDTH)
            drop["speed"] = random.uniform(2, 5)
            drop["color"] = random.choice(NEON_COLORS)
            drop["length"] = random.randint(10, 20)

        draw_glow(screen, drop["color"], (drop["x"], drop["y"]), 10)
        pygame.draw.line(
            screen,
            drop["color"],
            (drop["x"], drop["y"]),
            (drop["x"], drop["y"] + drop["length"]),
            2
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
