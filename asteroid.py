import CircleShape
import pygame
import constants
import random

class Asteroid(CircleShape.CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        for group in self.containers:
            group.add(self)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            v1 = self.velocity.rotate(new_angle)
            v2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x,self.position.y,new_radius)
            a2 = Asteroid(self.position.x,self.position.y,new_radius)
            a1.velocity = v1 * 1.2
            a2.velocity = v2