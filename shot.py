import CircleShape
import pygame
import constants

class Shot(CircleShape.CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        for group in self.containers:
            group.add(self)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,constants.SHOT_RADIUS,2)

    def update(self,dt):
        self.position += (self.velocity * dt)