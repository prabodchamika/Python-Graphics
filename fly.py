import pygame
import random
import time
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Rain with Lightning Shadows")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)  
BRIGHT_WHITE = (255, 255, 240) 

NUM_DROPS = 800  
DROP_WIDTH = 2
DROP_HEIGHT = 10
drops = []

class Drop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, HEIGHT)
        self.speed = random.randint(3, 6) 
        self.length = random.randint(8, 15)  
    
    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, -10)
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, DROP_WIDTH, self.length))

def lightning_flash():
   
    if random.random() < 0.05:
        flash_intensity = random.randint(50, 200) 
        flash_duration = random.randint(50, 150) 
        
        screen.fill(WHITE)
        pygame.display.update()
        pygame.time.delay(flash_duration)
        
        screen.fill(DARK_GRAY)
        pygame.display.update()
        pygame.time.delay(100) 

        for i in range(10):
            darken_amount = math.ceil(i * 25)
            screen.fill((max(0, 30 - darken_amount), max(0, 30 - darken_amount), max(0, 30 - darken_amount)))
            pygame.display.update()
            pygame.time.delay(15)

        screen.fill(BLACK)
        pygame.display.update()

for _ in range(NUM_DROPS):
    drops.append(Drop())

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for drop in drops:
        drop.fall()
        drop.draw()
    lightning_flash()
    pygame.display.flip()
    pygame.time.delay(15) 
    
pygame.quit()
