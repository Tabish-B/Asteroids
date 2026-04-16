from circleshape import *
import constants 
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.line_width = constants.LINE_WIDTH
    
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position , self.radius, self.line_width)
    
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if(self.radius <= constants.ASTEROID_MIN_RADIUS ):
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(angle) * 1.2
            velocity2 = self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = velocity1
        a2.velocity = velocity2
