import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        #self.rotation = 0 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return ""
        else:
            angle = random.uniform(20,50)
            v1,v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_r)
            a2 = Asteroid(self.position.x, self.position.y, new_r)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
            return ""

        