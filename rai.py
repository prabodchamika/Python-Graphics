import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 450, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Christmas Animation")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NEON_GREEN = (0, 255, 128)
NEON_BLUE = (0, 128, 255)
NEON_RED = (255, 0, 64)
NEON_YELLOW = (255, 255, 0)
NEON_ORANGE = (255, 165, 0)
SNOW_COLOR = (255, 255, 255)
SNOW_BLUE = (173, 216, 230) 
DARK_BLUE = (25, 25, 112) 
GOLD = (255, 215, 0) 

snowflakes = []

for _ in range(150):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, 0)
    size = random.randint(3, 6)  
    speed = random.randint(1, 2)  
    rotation = random.randint(0, 360)  
    glow = random.uniform(0.5, 1) 
    snowflakes.append([x, y, size, speed, rotation, glow])

def draw_tree(x, y):
    pygame.draw.polygon(screen, NEON_GREEN, [(x, y), (x - 60, y + 120), (x + 60, y + 120)])
    pygame.draw.polygon(screen, NEON_GREEN, [(x, y + 40), (x - 80, y + 160), (x + 80, y + 160)])
    pygame.draw.polygon(screen, NEON_GREEN, [(x, y + 80), (x - 100, y + 200), (x + 100, y + 200)])
    pygame.draw.polygon(screen, NEON_GREEN, [(x, y + 120), (x - 120, y + 240), (x + 120, y + 240)])
    
    pygame.draw.rect(screen, NEON_RED, (x - 15, y + 240, 30, 50))  

    for i in range(20):
        light_x = x + random.randint(-100, 100)
        light_y = y + random.randint(0, 240)
        color = random.choice([NEON_RED, NEON_YELLOW, NEON_GREEN, NEON_BLUE])
        light_size = random.randint(2, 5) 
        glow_intensity = random.uniform(0.5, 1)  
        glow_color = (int(glow_intensity * 255), int(glow_intensity * 255), int(glow_intensity * 255))
        pygame.draw.circle(screen, glow_color, (light_x, light_y), light_size)

    star_x = x
    star_y = y - 30
    pygame.draw.polygon(screen, NEON_YELLOW, [(star_x, star_y - 10), 
                                              (star_x - 10, star_y + 10),
                                              (star_x + 10, star_y + 10)])
    pygame.draw.polygon(screen, NEON_YELLOW, [(star_x, star_y - 5), 
                                              (star_x - 5, star_y + 5),
                                              (star_x + 5, star_y + 5)])
def draw_snowman(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 30)  
    pygame.draw.circle(screen, WHITE, (x, y + 50), 40)  
    pygame.draw.circle(screen, WHITE, (x, y + 120), 50)  
    pygame.draw.circle(screen, BLACK, (x - 10, y - 10), 5)  
    pygame.draw.circle(screen, BLACK, (x + 10, y - 10), 5) 
    pygame.draw.polygon(screen, NEON_ORANGE, [(x, y), (x + 20, y + 5), (x, y + 10)]) 
    pygame.draw.line(screen, BLACK, (x - 40, y + 50), (x - 70, y + 30), 3) 
    pygame.draw.line(screen, BLACK, (x + 40, y + 50), (x + 70, y + 30), 3) 
       
    pygame.draw.circle(screen, NEON_YELLOW, (x, y + 60), 5)
    pygame.draw.circle(screen, NEON_YELLOW, (x, y + 80), 5)
    pygame.draw.circle(screen, NEON_YELLOW, (x, y + 100), 5)
    
def draw_snow_ground():
    pygame.draw.rect(screen, SNOW_COLOR, (0, HEIGHT - 100, WIDTH, 100)) 

def draw_background():
    for y in range(HEIGHT):
        blue = min(255, 255 - (y // 3))  
        green = min(255, 255 - (y // 3))  
        color = (0, green, blue) 
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

def draw_snowflakes():
    for flake in snowflakes:
        flake[1] += flake[3]
        if flake[1] > HEIGHT:
            flake[1] = random.randint(-20, -1)
            flake[0] = random.randint(0, WIDTH)
        glow_intensity = int(flake[5] * 255)  
        pygame.draw.circle(screen, (glow_intensity, glow_intensity, glow_intensity), (flake[0], flake[1]), flake[2])

def draw_stars():
    for _ in range(10):
        star_x = random.randint(0, WIDTH)
        star_y = random.randint(0, HEIGHT // 2)  
        pygame.draw.circle(screen, WHITE, (star_x, star_y), random.randint(1, 3))

running = True

while running:
    screen.fill(DARK_BLUE) 
    draw_background()
    draw_snowflakes() 
    draw_stars() 
    draw_tree(WIDTH - 125, 310)
    draw_snowman(90, 440)
    draw_snow_ground()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30) 

pygame.quit()
