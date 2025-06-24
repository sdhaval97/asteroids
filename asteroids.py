from circleshape import *
from constants import *

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
        