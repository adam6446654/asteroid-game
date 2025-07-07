import CircleShape
import pygame

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