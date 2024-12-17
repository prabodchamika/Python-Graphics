import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fireworks Simulation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAX_PARTICLES = 200
GRAVITY = 0.05
FADE_RATE = 3
MAX_LIFETIME = 100 

class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.exploded = False
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.lifetime = random.randint(100, 200) 
        self.explosion_type = random.choice(['star', 'spiral', 'line'])  

    def update(self):
        if not self.exploded:
            self.y -= 2
            self.lifetime -= 1
            if self.lifetime <= 0:  
                self.exploded = True
                self.create_particles()
        else:
          
            for particle in self.particles:
                particle.update()
                if particle.alpha <= 0:
                    self.particles.remove(particle)

    def create_particles(self):
        num_particles = random.randint(100, MAX_PARTICLES) 
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 6)
            velocity = [math.cos(angle) * speed, math.sin(angle) * speed]
            if self.explosion_type == 'spiral':
                velocity[0] += random.uniform(-1, 1)
                velocity[1] += random.uniform(-1, 1)
            self.particles.append(Particle(self.x, self.y, self.color, velocity, self.explosion_type))

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 5) 
        for particle in self.particles:
            particle.draw(screen)

class Particle:
    def __init__(self, x, y, color, velocity, explosion_type):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.size = random.randint(2, 4)
        self.alpha = 255
        self.lifetime = MAX_LIFETIME
        self.explosion_type = explosion_type
        self.trail = []  

    def update(self):
        
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.velocity[1] += GRAVITY  
        self.alpha -= FADE_RATE  
        self.lifetime -= 1

        self.trail.append((self.x, self.y))
        if len(self.trail) > 10:
            self.trail.pop(0)

        if self.lifetime <= 0:
            self.alpha = 0 

    def draw(self, screen):
 
        if self.alpha > 0:
            particle_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, (*self.color, self.alpha), (self.size, self.size), self.size)
            screen.blit(particle_surface, (self.x - self.size, self.y - self.size))

     
            for pos in self.trail:
                pygame.draw.circle(screen, (*self.color, self.alpha // 2), pos, self.size // 2)

def main():
    clock = pygame.time.Clock()
    fireworks = []
    running = True

    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                fireworks.append(Firework(event.pos[0], event.pos[1]))

        if random.random() < 0.02:
            fireworks.append(Firework(random.randint(100, 1180), 720))
        
        for firework in fireworks:
            firework.update()
            firework.draw(screen)
        
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
