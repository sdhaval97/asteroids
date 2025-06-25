from circleshape import *
from constants import *
import random

class Asteroid(CircleShape, pygame.sprite.Sprite):
    containers = ()
    
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, radius)
        self.add(*self.containers)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)  
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        a1.velocity = vel1 * 1.2
        a2.velocity = vel2 * 1.2
        
        